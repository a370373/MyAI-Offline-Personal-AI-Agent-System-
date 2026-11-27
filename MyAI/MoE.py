
import atexit
import json
import os
import socket
import subprocess
import time
from pathlib import Path

import requests

from config import SYSTEM_PROMPT
from core.model import ask as ask_main


ROOT = Path(__file__).resolve().parent
EXPERT_DIR = ROOT / "expert"

LLAMA_SERVER_BIN = os.environ.get(
    "LLAMA_SERVER_BIN",
    "/opt/llama.cpp/llama-server"
)

MAIN_MODEL_URL = (
    "http://127.0.0.1:8080/v1/chat/completions"
)

STARTUP_TIMEOUT = 180
REQUEST_TIMEOUT = 300

_active_expert = None


def _log(message):
    print(f"[MoE] {message}", flush=True)


def _scan_experts():
    experts = []

    if not EXPERT_DIR.is_dir():
        return experts

    for index, directory in enumerate(
        sorted(EXPERT_DIR.iterdir())
    ):
        if not directory.is_dir():
            continue

        config_file = directory / "expert.json"

        if not config_file.is_file():
            continue

        try:
            config = json.loads(
                config_file.read_text(encoding="utf-8")
            )

            if not config.get("enabled", True):
                continue

            model_value = config.get("model")

            if model_value:
                model_path = Path(model_value)

                if not model_path.is_absolute():
                    model_path = directory / model_path
            else:
                models = sorted(directory.glob("*.gguf"))

                if len(models) != 1:
                    _log(
                        f"{directory.name}: "
                        "必須指定 model 或只放一個 GGUF"
                    )
                    continue

                model_path = models[0]

            model_path = model_path.resolve()

            if not model_path.is_file():
                _log(
                    f"{directory.name}: 找不到模型 {model_path}"
                )
                continue

            keywords = config.get("keywords", [])

            if not isinstance(keywords, list):
                continue

            experts.append({
                "name": config.get(
                    "name", directory.name
                ),
                "directory": directory,
                "model": model_path,
                "keywords": [
                    str(k).strip().casefold()
                    for k in keywords
                    if str(k).strip()
                ],
                "port": int(
                    config.get("port", 8101 + index)
                ),
                "ctx_size": int(
                    config.get("ctx_size", 8192)
                ),
                "gpu_layers": int(
                    config.get("n_gpu_layers", 0)
                ),
                "threads": int(
                    config.get("threads", 8)
                ),
            })

        except Exception as exc:
            _log(
                f"讀取 {config_file} 失敗：{exc}"
            )

    return experts


def _select_expert(user_text):
    text = str(user_text).casefold()
    candidates = []

    for expert in _scan_experts():
        matched = [
            keyword
            for keyword in expert["keywords"]
            if keyword in text
        ]

        if matched:
            score = (
                len(matched),
                sum(len(k) for k in matched)
            )

            candidates.append((score, expert))

    if not candidates:
        return None

    candidates.sort(
        key=lambda item: item[0],
        reverse=True
    )

    if (
        len(candidates) > 1
        and candidates[0][0] == candidates[1][0]
    ):
        _log("專家匹配分數相同，改用主模型")
        return None

    return candidates[0][1]


def _port_available(port):
    with socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    ) as sock:
        return sock.connect_ex(
            ("127.0.0.1", port)
        ) != 0


def _stop_active():
    global _active_expert

    if _active_expert is None:
        return

    process = _active_expert["process"]
    log_file = _active_expert["log_file"]

    if process.poll() is None:
        _log("正在關閉上一個專家模型")

        process.terminate()

        try:
            process.wait(timeout=8)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

    try:
        log_file.close()
    except Exception:
        pass

    _active_expert = None


def _start_expert(expert):
    global _active_expert

    if (
        _active_expert is not None
        and _active_expert["name"] == expert["name"]
        and _active_expert["process"].poll() is None
    ):
        return (
            f"http://127.0.0.1:"
            f"{expert['port']}/v1/chat/completions"
        )

    _stop_active()

    if not Path(LLAMA_SERVER_BIN).is_file():
        raise RuntimeError(
            f"找不到 llama-server：{LLAMA_SERVER_BIN}"
        )

    if not _port_available(expert["port"]):
        raise RuntimeError(
            f"專家 Port {expert['port']} 已被占用"
        )

    log_path = (
        expert["directory"] / "server.log"
    )

    log_file = open(log_path, "ab")

    command = [
        LLAMA_SERVER_BIN,
        "-m", str(expert["model"]),
        "--host", "127.0.0.1",
        "--port", str(expert["port"]),
        "-c", str(expert["ctx_size"]),
        "-ngl", str(expert["gpu_layers"]),
        "-t", str(expert["threads"]),
    ]

    _log(f"啟動專家：{expert['name']}")
    _log(f"模型：{expert['model']}")

    try:
        process = subprocess.Popen(
            command,
            stdin=subprocess.DEVNULL,
            stdout=log_file,
            stderr=subprocess.STDOUT,
            start_new_session=True
        )
    except Exception:
        log_file.close()
        raise

    _active_expert = {
        "name": expert["name"],
        "process": process,
        "log_file": log_file,
    }

    health_url = (
        f"http://127.0.0.1:"
        f"{expert['port']}/v1/models"
    )

    deadline = time.monotonic() + STARTUP_TIMEOUT

    while time.monotonic() < deadline:
        if process.poll() is not None:
            _stop_active()
            raise RuntimeError(
                f"專家 Server 提前退出，請檢查 {log_path}"
            )

        try:
            response = requests.get(
                health_url,
                timeout=2
            )

            if response.status_code == 200:
                _log("專家 Server 已就緒")
                return (
                    f"http://127.0.0.1:"
                    f"{expert['port']}/v1/chat/completions"
                )
        except requests.RequestException:
            pass

        time.sleep(1)

    _stop_active()

    raise TimeoutError(
        f"專家啟動超時，請檢查 {log_path}"
    )


def _ask_expert(url, context):
    payload = {
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": context
            }
        ],
        "temperature": 0.7
    }

    response = requests.post(
        url,
        json=payload,
        timeout=REQUEST_TIMEOUT
    )

    response.raise_for_status()

    result = response.json()

    if not result.get("choices"):
        raise RuntimeError(
            "專家模型沒有回傳 choices"
        )

    content = (
        result["choices"][0]
        .get("message", {})
        .get("content")
    )

    if not isinstance(content, str):
        raise RuntimeError(
            "專家模型回傳格式錯誤"
        )

    return content


def route_request(context):
    expert = _select_expert(context)

    if expert is None:
        _stop_active()
        _log("沒有匹配專家，使用主模型")
        return ask_main(context)

    try:
        url = _start_expert(expert)

        _log(f"交由專家處理：{expert['name']}")

        return _ask_expert(url, context)

    except Exception as exc:
        _log(f"專家處理失敗：{exc}")
        _stop_active()
        _log("回退至主模型 8080")

        return ask_main(context)


atexit.register(_stop_active)

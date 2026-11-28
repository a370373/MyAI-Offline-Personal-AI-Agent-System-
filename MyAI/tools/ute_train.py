import json
import os
import re
import shutil
import signal
import subprocess
import time
import uuid
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parent
MYAI_ROOT = TOOLS_DIR.parent
CONFIG_FILE = TOOLS_DIR / "ute_config.json"
EXPERT_DIR = MYAI_ROOT / "expert"
LOCK_FILE = MYAI_ROOT / "ute_train.lock"


class WorkflowError(Exception):
    pass


def _load_config():
    if not CONFIG_FILE.is_file():
        raise WorkflowError("找不到 ute_config.json")

    try:
        config = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except Exception as exc:
        raise WorkflowError(f"設定檔讀取失敗：{exc}")

    if not isinstance(config, dict):
        raise WorkflowError("設定檔格式錯誤")

    if not config.get("enabled", False):
        raise WorkflowError("UTE 整合目前未啟用")

    return config


def _path(value, required=True):
    if not isinstance(value, str) or not value.strip():
        if required:
            raise WorkflowError("必要路徑尚未設定")
        return None

    result = Path(value).expanduser()

    if not result.is_absolute():
        result = MYAI_ROOT / result

    return result.resolve()


def _write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)

    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    os.replace(temporary, path)


def _tail(path, lines=30):
    try:
        content = path.read_text(
            encoding="utf-8",
            errors="replace"
        ).splitlines()

        return "\n".join(content[-lines:])
    except Exception:
        return ""


def _terminate_group(process):
    if process.poll() is not None:
        return

    try:
        os.killpg(process.pid, signal.SIGTERM)
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait()
    except ProcessLookupError:
        pass


def _run_command(command, cwd, timeout, log_file, stage):
    if not command:
        raise WorkflowError(f"{stage} 命令為空")

    with log_file.open("a", encoding="utf-8") as log:
        log.write(
            f"\n\n===== {stage} =====\n"
            f"COMMAND: {command!r}\n"
        )
        log.flush()

        process = subprocess.Popen(
            command,
            cwd=str(cwd),
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True
        )

        try:
            return_code = process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            _terminate_group(process)
            raise WorkflowError(f"{stage} 執行逾時")
        except BaseException:
            _terminate_group(process)
            raise

    if return_code != 0:
        raise WorkflowError(
            f"{stage} 失敗，exit code={return_code}\n"
            f"{_tail(log_file)}"
        )


def _validate_expert(config):
    expert = config.get("expert", {})

    name = expert.get("name", "")

    if not isinstance(name, str) or not re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}",
        name
    ):
        raise WorkflowError("Expert 名稱格式不合法")

    keywords = expert.get("keywords", [])

    if (
        not isinstance(keywords, list)
        or not keywords
        or not all(
            isinstance(x, str) and x.strip()
            for x in keywords
        )
    ):
        raise WorkflowError("Expert keywords 必須是非空字串陣列")

    port = int(expert.get("port", 8101))

    if not 1 <= port <= 65535:
        raise WorkflowError("Expert port 超出有效範圍")

    return expert


def _check_adapter(adapter_dir):
    report = adapter_dir / "adapter_verification.json"

    if not report.is_file():
        raise WorkflowError("找不到 Adapter 驗證報告")

    try:
        result = json.loads(report.read_text(encoding="utf-8"))
    except Exception as exc:
        raise WorkflowError(f"Adapter 驗證報告無法解析：{exc}")

    if result.get("status") != "passed":
        raise WorkflowError("Adapter 驗證未通過")

    if not (adapter_dir / "adapter_config.json").is_file():
        raise WorkflowError("Adapter 缺少 adapter_config.json")


def _validate_gguf(path):
    if not path.is_file():
        raise WorkflowError("GGUF 檔案不存在")

    if path.stat().st_size <= 4:
        raise WorkflowError("GGUF 檔案大小異常")

    with path.open("rb") as file:
        if file.read(4) != b"GGUF":
            raise WorkflowError("GGUF Magic 驗證失敗")


def _register_expert(gguf_path, final_dir, expert):
    if final_dir.exists():
        raise WorkflowError(
            f"Expert 目錄已存在，不覆蓋：{final_dir}"
        )

    final_dir.mkdir(parents=True, exist_ok=False)
    moved_model = final_dir / gguf_path.name

    try:
        os.replace(gguf_path, moved_model)

        expert_config = {
            "enabled": True,
            "name": expert["name"],
            "model": moved_model.name,
            "keywords": expert["keywords"],
            "port": int(expert.get("port", 8101)),
            "ctx_size": int(expert.get("ctx_size", 8192)),
            "n_gpu_layers": int(
                expert.get("n_gpu_layers", 0)
            ),
            "threads": int(expert.get("threads", 8))
        }

        _write_json(
            final_dir / "expert.json",
            expert_config
        )

        return moved_model

    except Exception:
        shutil.rmtree(final_dir, ignore_errors=True)
        raise


def run(**_ignored):
    job_id = uuid.uuid4().hex
    current_stage = "INITIALIZING"
    lock_fd = None
    lock_acquired = False

    try:
        lock_fd = os.open(
            str(LOCK_FILE),
            os.O_CREAT | os.O_EXCL | os.O_WRONLY,
            0o600
        )

        os.write(lock_fd, job_id.encode("ascii"))
        os.close(lock_fd)
        lock_fd = None
        lock_acquired = True

        config = _load_config()
        expert = _validate_expert(config)

        paths = config.get("paths", {})
        training = config.get("training", {})
        merge = config.get("merge", {})
        gguf = config.get("gguf", {})
        workflow = config.get("workflow", {})

        ute_root = _path(paths.get("ute_root"))
        python = paths.get("python", "python3")
        llama_cpp = _path(paths.get("llama_cpp"))

        quantize_bin = _path(
            paths.get("quantize_bin"),
            required=False
        )

        scripts = [
            ute_root / "train.py",
            ute_root / "tools/merge_adapter.py",
            ute_root / "tools/convert_gguf.py"
        ]

        for script in scripts:
            if not script.is_file():
                raise WorkflowError(f"找不到 UTE 腳本：{script}")

        if not (llama_cpp / "convert_hf_to_gguf.py").is_file():
            raise WorkflowError("llama.cpp 缺少 convert_hf_to_gguf.py")

        model = training.get("model")
        data_dir = _path(training.get("data_dir"))

        if not isinstance(model, str) or not model.strip():
            raise WorkflowError("training.model 尚未設定")

        if not data_dir.is_dir():
            raise WorkflowError("訓練資料目錄不存在")

        workspace = _path(paths.get("workspace"))
        logs_dir = _path(paths.get("logs"))

        workspace.mkdir(parents=True, exist_ok=True)
        logs_dir.mkdir(parents=True, exist_ok=True)

        log_file = logs_dir / f"{job_id}.log"
        status_file = logs_dir / f"{job_id}.json"

        job_dir = workspace / job_id
        job_dir.mkdir(parents=True, exist_ok=False)

        adapter_dir = job_dir / "adapter"
        merged_dir = job_dir / "merged"

        EXPERT_DIR.mkdir(parents=True, exist_ok=True)

        staging_root = EXPERT_DIR / ".staging"
        staging_root.mkdir(parents=True, exist_ok=True)

        staging_dir = staging_root / job_id
        staging_dir.mkdir(parents=True, exist_ok=False)

        gguf_path = staging_dir / f"{expert['name']}.gguf"
        final_dir = EXPERT_DIR / expert["name"]

        timeouts = workflow.get("timeout_seconds", {})

        def stage(name):
            nonlocal current_stage
            current_stage = name

            _write_json(status_file, {
                "job_id": job_id,
                "stage": current_stage,
                "updated_at": time.time()
            })

        # TRAINING
        stage("TRAINING")

        train_cmd = [
            python,
            str(ute_root / "train.py"),
            "--model", model,
            "--data-dir", str(data_dir),
            "--output-dir", str(adapter_dir),
            "--epochs", str(training.get("epochs", 3.0)),
            "--learning-rate", str(
                training.get("learning_rate", 0.0001)
            ),
            "--max-length", str(training.get("max_length", 1024)),
            "--batch-size", str(training.get("batch_size", 1)),
            "--gradient-accumulation", str(
                training.get("gradient_accumulation", 4)
            ),
            "--lora-r", str(training.get("lora_r", 16)),
            "--lora-alpha", str(training.get("lora_alpha", 32)),
            "--lora-dropout", str(
                training.get("lora_dropout", 0.05)
            ),
            "--quantization", str(
                training.get("quantization", "none")
            ),
            "--quant-type", str(
                training.get("quant_type", "nf4")
            ),
            "--compute-dtype", str(
                training.get("compute_dtype", "auto")
            ),
            "--target-modules", str(
                training.get("target_modules", "all-linear")
            ),
            "--cpu-threads", str(
                training.get("cpu_threads", 4)
            ),
            "--seed", str(training.get("seed", 42))
        ]

        if training.get("train_embeddings"):
            train_cmd.append("--train-embeddings")

        train_cmd.append(
            "--double-quant"
            if training.get("double_quant", True)
            else "--no-double-quant"
        )

        resume = training.get("resume_checkpoint")

        if resume:
            train_cmd.extend([
                "--resume-checkpoint",
                str(resume)
            ])

        _run_command(
            train_cmd,
            ute_root,
            int(timeouts.get("training", 86400)),
            log_file,
            current_stage
        )

        _check_adapter(adapter_dir)

        # MERGING
        stage("MERGING")

        merge_cmd = [
            python,
            str(ute_root / "tools/merge_adapter.py"),
            "--base-model", model,
            "--adapter", str(adapter_dir),
            "--output", str(merged_dir),
            "--dtype", str(merge.get("dtype", "auto"))
        ]

        if merge.get("trust_remote_code"):
            merge_cmd.append("--trust-remote-code")

        _run_command(
            merge_cmd,
            ute_root,
            int(timeouts.get("merge", 43200)),
            log_file,
            current_stage
        )

        if not (merged_dir / "config.json").is_file():
            raise WorkflowError("Merged model 缺少 config.json")

        if not list(merged_dir.glob("*.safetensors")):
            raise WorkflowError("Merged model 缺少 safetensors")

        # GGUF CONVERSION
        stage("GGUF_CONVERSION")

        convert_cmd = [
            python,
            str(ute_root / "tools/convert_gguf.py"),
            "--model", str(merged_dir),
            "--output", str(gguf_path),
            "--llama-cpp", str(llama_cpp),
            "--outtype", str(gguf.get("outtype", "f16")),
            "--python", python
        ]

        quantization = gguf.get("quantization")

        if quantization:
            convert_cmd.extend([
                "--quantization", str(quantization)
            ])

            if not quantize_bin:
                raise WorkflowError(
                    "GGUF 量化已啟用，但 quantize_bin 尚未設定"
                )

            convert_cmd.extend([
                "--quantize-bin",
                str(quantize_bin)
            ])

        if gguf.get("keep_f16"):
            convert_cmd.append("--keep-f16")

        _run_command(
            convert_cmd,
            ute_root,
            int(timeouts.get("gguf", 43200)),
            log_file,
            current_stage
        )

        # VALIDATING
        stage("VALIDATING")
        _validate_gguf(gguf_path)

        # REGISTERING EXPERT
        if workflow.get("register_expert", True):
            stage("REGISTERING_EXPERT")

            _register_expert(
                gguf_path,
                final_dir,
                expert
            )

        # CLEANUP
        stage("CLEANUP")

        if workflow.get("cleanup_intermediates", True):
            shutil.rmtree(adapter_dir, ignore_errors=True)
            shutil.rmtree(merged_dir, ignore_errors=True)

        shutil.rmtree(staging_dir, ignore_errors=True)

        stage("IDLE")

        return {
            "success": True,
            "job_id": job_id,
            "expert": expert["name"],
            "directory": (
                str(final_dir)
                if workflow.get("register_expert", True)
                else None
            ),
            "log": str(log_file),
            "message": "UTE 訓練、合併、GGUF 驗證及 Expert 註冊完成"
        }

    except Exception as exc:
        return {
            "success": False,
            "job_id": job_id,
            "stage": current_stage,
            "error": str(exc),
            "message": "UTE 工作流程失敗；中間產物保留供檢查"
        }

    finally:
        if lock_fd is not None:
            os.close(lock_fd)

        if lock_acquired:
            try:
                LOCK_FILE.unlink(missing_ok=True)
            except Exception:
                pass

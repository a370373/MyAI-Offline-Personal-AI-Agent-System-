import hashlib
import json
import re

from pathlib import Path

from core.agent_core import handle
from core.action_controller import action_budget

from context_manager import (
    get_pending_action,
    clear_pending_action,
)


BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = BASE_DIR / "config" / "goal_config.json"

CONFIRM_WORDS = {
    "可以", "好", "允許", "確認", "執行", "開始"
}

CANCEL_WORDS = {
    "取消", "拒絕", "不要", "停止", "cancel", "no"
}


def load_config():

    defaults = {
        "enabled": True,
        "max_reflections": 10,
        "max_tool_calls": 20,
        "allow_retry": True,
        "detect_repeated_actions": True,
    }

    try:
        with CONFIG_PATH.open(
            "r",
            encoding="utf-8",
        ) as f:
            data = json.load(f)

        if not isinstance(data, dict):
            raise ValueError("設定檔必須是 JSON object")

        defaults.update(data)

    except FileNotFoundError:
        pass

    except Exception as exc:
        print("[Goal Config Error]", exc)

    defaults["max_reflections"] = max(
        1,
        int(defaults["max_reflections"]),
    )

    defaults["max_tool_calls"] = max(
        0,
        int(defaults["max_tool_calls"]),
    )

    return defaults


def fingerprint(action):

    raw = json.dumps(
        action,
        ensure_ascii=False,
        sort_keys=True,
        default=str,
    )

    return hashlib.sha256(
        raw.encode("utf-8")
    ).hexdigest()


def extract_decision(text):

    if not isinstance(text, str):
        return None

    match = re.search(
        r"<goal_decision>\s*(.*?)\s*</goal_decision>",
        text,
        flags=re.DOTALL,
    )

    if not match:
        return None

    try:
        decision = json.loads(match.group(1))

    except Exception:
        return None

    if not isinstance(decision, dict):
        return None

    if decision.get("status") not in {
        "complete",
        "continue",
        "stop",
    }:
        return None

    if not isinstance(
        decision.get("goal_completed", False),
        bool,
    ):
        return None

    return decision


def build_reflection_prompt(
    goal,
    history,
    round_number,
    max_rounds,
    allow_retry,
):
    previous = []

    for item in history[-8:]:
        round_id = item.get("round", "?")
        phase = item.get("phase", "result")
        result = item.get("result", "")

        previous.append(
            f"第 {round_id} 輪（{phase}）：\n\n{result}\n"
        )

    history_text = "\n".join(previous)

    retry_text = "是" if allow_retry else "否"

    return "\n".join([
        "你現在正在執行 MyAI Goal Mode。",
        "",
        "## 目標",
        "",
        str(goal),
        "",
        "## 目前進度",
        "",
        f"目前反思輪次：{round_number}/{max_rounds}",
        f"是否允許重試：{retry_text}",
        "",
        "## 歷史紀錄",
        "",
        history_text if history_text else "目前沒有執行紀錄。",
        "",
        "## 你的任務",
        "",
        "根據目標、歷史紀錄及實際執行結果判斷下一步。",
        "1. 檢查目標是否真正完成。",
        "2. 尚未完成時，決定合理的下一步。",
        "3. 必要時調整策略。",
        "4. 只有允許重試時才提出重試。",
        "5. 無法安全或合理繼續時停止。",
        "6. 不要重複已完成的操作。",
        "7. 不要把未驗證的事情宣稱為成功。",
        "",
        "## 工具與權限規則",
        "",
        "- 使用 MyAI 原本的工具呼叫格式。",
        "- 不得假造工具執行結果。",
        "- 不得偽造使用者確認。",
        "- 需要使用者確認時，等待原本的 pending action 流程。",
        "- 不得假設尚未執行的操作已經成功。",
        "- 根據實際工具結果更新判斷。",
        "",
        "## 決策輸出格式",
        "",
        "最後必須輸出以下標記，標記內只能包含合法 JSON：",
        "",
        "<goal_decision>",
        "{",
        '    "status": "continue",',
        '    "reason": "判斷理由",',
        '    "next_step": "下一步行動",',
        '    "goal_completed": false,',
        '    "user_summary": ""',
        "}",
        "</goal_decision>",
        "",
        "status 只能是 complete、continue、stop。",
        "complete 必須將 goal_completed 設為 true。",
        "continue 和 stop 必須將 goal_completed 設為 false。",
        "complete 或 stop 時，user_summary 必須提供給使用者看的結果。",
        "不得只因為執行某項操作，就認定整個目標完成。",
    ])


def confirm_pending_action(
    action,
    input_fn=input,
    output_fn=print,
):

    output_fn("\n[GOAL MODE] 操作需要使用者確認。")

    output_fn(
        json.dumps(
            action,
            ensure_ascii=False,
            indent=2,
            default=str,
        )
    )

    while True:

        answer = input_fn(
            "\n是否允許執行？（確認 / 取消）："
        ).strip()

        if answer in CONFIRM_WORDS:
            return True

        if answer in CANCEL_WORDS:
            return False

        output_fn("請輸入「確認」或「取消」。")


def run_goal(
    goal,
    runtime=None,
    input_fn=input,
    output_fn=print,
):
    config = load_config()

    if not config["enabled"]:
        return "Goal Mode 目前已停用。"

    goal = goal.strip()

    if not goal:
        return "請提供目標。"

    if get_pending_action():
        return (
            "目前已有待確認操作。"
            "請先處理原本的 pending action，再啟動 Goal Mode。"
        )

    max_reflections = config["max_reflections"]

    history = []
    seen_pending = set()

    final_summary = ""
    last_result = ""
    stop_reason = ""

    def record(round_number, phase, result):
        history.append({
            "round": round_number,
            "phase": phase,
            "result": str(result),
        })

    output_fn("\n[GOAL MODE START]")
    output_fn(f"目標：{goal}")

    with action_budget(
        config["max_tool_calls"],
        config["detect_repeated_actions"],
    ) as budget:

        for round_number in range(1, max_reflections + 1):

            output_fn(
                f"\n[GOAL REFLECTION "
                f"{round_number}/{max_reflections}]"
            )

            prompt = build_reflection_prompt(
                goal,
                history,
                round_number,
                max_reflections,
                config["allow_retry"],
            )

            # 取得模型原始反思結果。
            try:
                last_result = str(handle(prompt, runtime))

            except Exception as exc:
                last_result = f"Goal Mode 執行錯誤：{exc}"

                record(
                    round_number,
                    "reflection_error",
                    last_result,
                )

                if not config["allow_retry"]:
                    stop_reason = "執行錯誤且未允許重試。"
                    break

                continue

            # 每輪原始結果只記錄一次。
            record(
                round_number,
                "reflection",
                last_result,
            )

            # 檢查 pending action。
            pending = get_pending_action()

            if pending:

                pending_id = fingerprint(pending)

                if (
                    config["detect_repeated_actions"]
                    and pending_id in seen_pending
                ):
                    clear_pending_action()

                    last_result = (
                        "偵測到重複的待執行操作，"
                        "為避免循環，已停止。"
                    )

                    record(
                        round_number,
                        "pending_rejected",
                        last_result,
                    )

                    stop_reason = last_result
                    break

                seen_pending.add(pending_id)

                if budget["used"] >= budget["limit"]:
                    clear_pending_action()

                    last_result = (
                        "已達 Goal Mode 工具執行額度，"
                        "這項操作沒有執行。"
                    )

                    record(
                        round_number,
                        "pending_budget_exceeded",
                        last_result,
                    )

                    stop_reason = last_result
                    break

                approved = confirm_pending_action(
                    pending,
                    input_fn,
                    output_fn,
                )

                if not approved:
                    clear_pending_action()

                    last_result = "使用者取消了這項操作。"

                    record(
                        round_number,
                        "pending_cancelled",
                        last_result,
                    )

                else:
                    try:
                        # 沿用原本 pending action 確認流程。
                        last_result = str(handle("確認", runtime))

                    except Exception as exc:
                        last_result = f"確認執行時發生錯誤：{exc}"

                    record(
                        round_number,
                        "pending_execution",
                        last_result,
                    )

                    if get_pending_action():
                        stop_reason = (
                            "確認流程未完成 pending action，"
                            "Goal Mode 已暫停。"
                        )

                        record(
                            round_number,
                            "pending_incomplete",
                            stop_reason,
                        )

                        break

                if budget["used"] >= budget["limit"]:
                    stop_reason = "已達 Goal Mode 工具執行額度。"

                    record(
                        round_number,
                        "budget_exceeded",
                        stop_reason,
                    )

                    break

                # pending action 處理完成，進入下一輪反思。
                continue

            # 解析模型決策。
            decision = extract_decision(last_result)

            if decision is None:
                output_fn(
                    "[GOAL MODE] "
                    "沒有取得有效決策標記，"
                    "本輪結果不視為完成。"
                )
                continue

            status = decision["status"]

            if status == "complete":

                if decision.get("goal_completed") is not True:
                    output_fn(
                        "[GOAL MODE] "
                        "模型宣稱完成，但未提供完成標記。"
                    )
                    continue

                final_summary = str(
                    decision.get("user_summary", "")
                ).strip()

                if not final_summary:
                    final_summary = last_result

                output_fn("[GOAL MODE COMPLETE]")
                break

            if status == "stop":

                final_summary = str(
                    decision.get("user_summary", "")
                ).strip()

                if not final_summary:
                    final_summary = last_result

                stop_reason = str(
                    decision.get("reason", "模型決定停止。")
                )

                output_fn("[GOAL MODE STOPPED]")
                break

            if status == "continue":
                output_fn(
                    "[GOAL MODE] "
                    + str(decision.get("reason", "繼續執行"))
                )
                continue

        else:
            stop_reason = "已達到最大反思次數。"

    if not final_summary:
        final_summary = (
            "Goal Mode 已停止。\n"
            + (stop_reason + "\n\n" if stop_reason else "")
            + "目前最後一次取得的結果：\n\n"
            + last_result
        )

    output_fn("\n[GOAL MODE FINISHED]")

    return final_summary

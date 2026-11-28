import contextvars
import hashlib
import json

from contextlib import contextmanager

from core.tool_manager import run_tool
from core.action_executor import ActionExecutor


MAX_ACTIONS = 10

_ACTIVE_ACTION_BUDGET = contextvars.ContextVar(
    "myai_goal_action_budget",
    default=None,
)


@contextmanager
def action_budget(limit, detect_repeated=True):
    state = {
        "limit": max(0, int(limit)),
        "used": 0,
        "detect_repeated": bool(detect_repeated),
        "seen": set(),
        "blocked_reason": None,
    }

    token = _ACTIVE_ACTION_BUDGET.set(state)

    try:
        yield state
    finally:
        _ACTIVE_ACTION_BUDGET.reset(token)


def _fingerprint(item):
    raw = json.dumps(
        item,
        ensure_ascii=False,
        sort_keys=True,
        default=str,
    )

    return hashlib.sha256(
        raw.encode("utf-8")
    ).hexdigest()


def execute_actions(actions, browser=None):

    print("[DEBUG execute_actions input]", actions)

    results = []

    executor = None

    if browser:
        executor = ActionExecutor(browser)

    count = 0
    blocked = False

    budget = _ACTIVE_ACTION_BUDGET.get()

    def reserve(item):
        nonlocal count

        if count >= MAX_ACTIONS:
            return False, "單次工具呼叫已達 MAX_ACTIONS 限制"

        if budget is not None:

            if budget["used"] >= budget["limit"]:
                return False, "Goal Mode 已達工具執行次數上限"

            fingerprint = _fingerprint(item)

            if (
                budget["detect_repeated"]
                and fingerprint in budget["seen"]
            ):
                return False, "Goal Mode 偵測到重複工具操作"

            budget["seen"].add(fingerprint)
            budget["used"] += 1

        count += 1

        return True, None

    def blocked_result(reason):
        return {
            "success": False,
            "blocked": True,
            "error": reason,
        }

    for item in actions:

        if count >= MAX_ACTIONS:
            break

        # Browser 單一 action
        if (
            isinstance(item, dict)
            and item.get("tool") == "browser"
            and "action" in item
        ):

            allowed, reason = reserve(item)

            if not allowed:
                results.append(blocked_result(reason))
                blocked = True
                break

            if executor:
                result = executor.execute(item)
            else:
                result = {
                    "success": False,
                    "error": "no browser executor",
                }

            results.append(result)

            continue

        # 舊版 Browser wrapper 格式
        if (
            isinstance(item, dict)
            and item.get("tool") == "browser"
            and "actions" in item
        ):

            for action in item["actions"]:

                allowed, reason = reserve(action)

                if not allowed:
                    results.append(blocked_result(reason))
                    blocked = True
                    break

                if executor:
                    result = executor.execute(action)
                else:
                    result = {
                        "success": False,
                        "error": "no browser executor",
                    }

                results.append(result)

            if blocked:
                break

            continue

        # 一般工具
        allowed, reason = reserve(item)

        if not allowed:
            results.append(blocked_result(reason))
            blocked = True
            break

        result = run_tool(item)

        results.append(result)

    print("[DEBUG execute_actions output]", results)

    return results

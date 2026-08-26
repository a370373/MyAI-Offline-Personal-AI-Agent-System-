def normalize_action(action):

    if not isinstance(action, dict):
        return {
            "action": "unknown"
        }


    # 修復 LLM 巢狀 action
    while isinstance(action.get("action"), dict):

        action = action["action"]


    # action 名稱統一

    name = action.get(
        "action",
        ""
    )


    aliases = {

        "click_element":
            "click",

        "clickElement":
            "click",

        "input":
            "type",

        "write":
            "type",

        "navigate":
            "open",

        "click":
            "click_element",

        "tap":
            "click_element",

        "press":
            "press_enter",

        "enter":
            "press_enter",

        "sleep":
            "wait",

        "delay":
            "wait",

        "wait_page":
            "wait",

        "scroll_down":
            "scroll",

        "scroll_up":
            "scroll",

        "reload":
            "refresh",

        "go_back":
            "back"

    }


    if name in aliases:

        action["action"] = aliases[name]



    
    # click target 自動補齊
    if action.get("action") == "click_element":

        if "target" not in action:

            if "element" in action:
                action["target"] = action["element"]

    
    # type 欄位統一
    if action.get("action") == "type":

        if "text" not in action:

            action["text"] = action.get(
                "value",
                ""
            )


    return action

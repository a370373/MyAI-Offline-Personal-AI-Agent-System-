def analyze(action):

    if not isinstance(action, dict):

        return {
            "level": "HIGH",
            "reason": "未知操作格式"
        }


    tool = action.get(
        "tool"
    )

    command = action.get(
        "command",
        ""
    )


    # ====================
    # Browser 舊格式相容
    # ====================

    if tool == "browser" and command:

        open_words = [
            "open",
            "打開",
            "開啟"
        ]

        for word in open_words:

            if command.startswith(word):

                action["action"] = "open"

                action["url"] = command[
                    len(word):
                ].strip()

                break



    # ====================
    # 低風險工具
    # ====================

    if tool in [
        "system_info",
        "current_time",
        "file_manager",
        "project_scanner",
        "knowledge_search",
        "browser"
    ]:

        return {
            "level": "LOW",
            "reason": "安全查詢操作"
        }



    # ====================
    # Browser
    # ====================

    if tool == "browser":

        action_name = action.get(
            "action",
            ""
        )


        if action_name in [
            "open",
            "read",
            "search"
        ]:

            return {
                "level": "LOW",
                "reason": "瀏覽查詢操作"
            }


        if action_name in [
            "click",
            "type"
        ]:

            return {
                "level": "MEDIUM",
                "reason": "瀏覽器互動操作"
            }


        return {
            "level": "MEDIUM",
            "reason": "瀏覽器操作需要確認"
        }



    # ====================
    # Shell
    # ====================

    if tool == "shell":

        dangerous = [
            "rm ",
            "delete",
            "chmod",
            "pkg install",
            "apt install"
        ]


        for word in dangerous:

            if word in command:

                return {
                    "level": "HIGH",
                    "reason": f"危險指令:{word}"
                }


        return {
            "level": "MEDIUM",
            "reason": "Shell操作需要確認"
        }



    # ====================
    # Memory
    # ====================

    if tool == "memory":

        return {
            "level": "MEDIUM",
            "reason": "修改長期記憶"
        }



    return {
        "level": "MEDIUM",
        "reason": "未知工具"
    }

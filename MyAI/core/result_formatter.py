def format_result(result):

    if not isinstance(result, dict):
        return "操作完成。"

    if not result.get("success"):
        error = result.get(
            "error",
            "未知錯誤"
        )

        return f"操作失敗：{error}"


    tool = result.get(
        "tool",
        ""
    )

    action = result.get(
        "action",
        ""
    )

    data = result.get(
        "data",
        {}
    )


    # browser
    if tool == "browser":

        if isinstance(data, dict):

            url = data.get(
                "url",
                ""
            )

            title = data.get(
                "title",
                ""
            )

            if action in ["open", "run"]:

                if url:
                    return f"已完成，已開啟 {url}"

                if title:
                    return f"已完成，已開啟頁面：{title}"


        return "瀏覽器操作已完成。"


    # shell
    if tool == "shell":

        if isinstance(data, dict):

            output = data.get(
                "stdout",
                ""
            )

            if output:
                return f"命令執行完成：\n{output}"


        return "命令執行完成。"


    # file
    if tool == "file_manager":

        return "檔案操作已完成。"


    # default

    return f"{tool} 操作已完成。"

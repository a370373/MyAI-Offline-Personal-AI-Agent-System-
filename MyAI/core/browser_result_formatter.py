def format_browser_result(result, observation):

    messages = []

    if isinstance(result, list):

        for item in result:

            if not isinstance(item, dict):
                continue

            if item.get("success"):

                action = item.get("action")

                if action == "find_element":
                    messages.append(
                        "找到指定網頁元素"
                    )

                elif action == "type":
                    messages.append(
                        f"輸入文字成功：{item.get('text','')}"
                    )

                elif action == "submit":
                    messages.append(
                        "送出操作成功"
                    )

            elif item.get("error"):

                messages.append(
                    f"操作失敗：{item.get('error')}"
                )


    if observation:

        dom = observation.get(
            "dom_after_action",
            []
        )

        if dom:

            messages.append(
                "已重新讀取 DOM 狀態"
            )


    if messages:

        return (
            "瀏覽器任務結果：\n"
            +
            "\n".join(
                "- " + x
                for x in messages
            )
        )


    return "瀏覽器任務沒有可確認結果。"

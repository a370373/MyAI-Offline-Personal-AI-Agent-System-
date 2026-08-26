def validate(action, history):

    if not action:

        return {
            "action":"stop",
            "reason":"empty action"
        }


    current = action.get(
        "action"
    )


    # 防止連續 open 同網址

    if current == "open":

        url = action.get(
            "url",
            ""
        )


        for item in history:

            old = item.get(
                "action",
                {}
            )


            if (
                old.get("action") == "open"
                and old.get("url") == url
            ):

                return {
                    "action":"read",
                    "reason":"already opened"
                }



    # 防止重複 click 同元素

    if current in (
        "click",
        "click_element"
    ):

        target = action.get(
            "target",
            ""
        )


        for item in history:

            old=item.get(
                "action",
                {}
            )


            if (
                old.get("action") == current
                and old.get("target") == target
            ):

                return {
                    "action":"read",
                    "reason":"duplicate click"
                }



    return action

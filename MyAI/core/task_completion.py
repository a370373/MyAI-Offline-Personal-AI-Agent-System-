def check_complete(
    goal,
    history,
    result,
    dom=None
):


    goal=goal.lower()


    # 沒成功不用判斷

    if isinstance(result,dict):

        if result.get("success") is False:

            return False



    actions=[]


    for h in history:

        if isinstance(h,dict):

            a=h.get(
                "action",
                {}
            )

            if isinstance(a,dict):

                actions.append(
                    a.get(
                        "action",
                        ""
                    )
                )


    current=result.get(
        "action",
        ""
    ) if isinstance(result,dict) else ""



    actions.append(
        current
    )



    # ==================
    # 搜尋任務
    # ==================

    if (
        "搜尋" in goal
        or
        "search" in goal
    ):


        has_type = (
            "type" in actions
        )


        has_enter = (
            "press_enter" in actions
            or
            "submit" in actions
        )


        if has_type and has_enter:

            print(
                "[COMPLETE] search"
            )

            return True



    # ==================
    # 開啟網站
    # ==================

    if (
        "打開" in goal
        or
        "open" in goal
    ):


        if "open" in actions:

            print(
                "[COMPLETE] open"
            )

            return True



    # ==================
    # 輸入
    # ==================

    if (
        "輸入" in goal
    ):


        if "type" in actions:

            print(
                "[COMPLETE] type"
            )

            return True



    return False

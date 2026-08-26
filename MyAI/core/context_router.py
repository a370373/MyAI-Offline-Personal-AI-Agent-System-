from core.short_context import load_context


def get_relevant_context(user_input):

    context = load_context()


    if not context:

        return None



    follow_words = [

        "結果如何",
        "結果呢",
        "剛剛",
        "上一個",
        "完成了嗎",
        "成功嗎",
        "狀態",
        "怎樣"

    ]



    if any(
        x in user_input
        for x in follow_words
    ):

        return context



    last_task = context.get(
        "last_task",
        ""
    )



    if last_task == "browser":

        browser_words = [

            "網頁",
            "瀏覽器",
            "網站",
            "那個",
            "剛才輸入",
            "點擊"

        ]


        if any(
            x in user_input
            for x in browser_words
        ):

            return context



    return None

from core.short_context import load_context


FOLLOW_UP_WORDS = [
    "結果如何",
    "怎麼樣",
    "怎樣了",
    "完成了嗎",
    "成功嗎",
    "狀態",
    "如何",
    "然後呢",
    "呢"
]


def is_follow_up(text):

    for word in FOLLOW_UP_WORDS:
        if word in text:
            return True

    return False



def get_follow_up_context(user_input):

    if not is_follow_up(user_input):
        return None


    context = load_context()


    if not context:
        return None


    if context.get(
        "last_task"
    ) != "browser":

        return None


    return {

        "type": "follow_up_browser",

        "data": context

    }

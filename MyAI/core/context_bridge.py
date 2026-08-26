from context_manager import (
    build_prompt_context,
    get_pending_action,
    set_pending_action,
    clear_pending_action
)


def inject_context(user_input, extra=None):

    context = build_prompt_context(
        user_input
    )

    if extra:

        context += "\n\n目前執行狀態:\n"
        context += str(extra)


    pending = get_pending_action()

    if pending:

        context += """

目前有等待確認操作：

%s

如果使用者回答：
好 / 可以 / 確認 / 允許

代表允許繼續。
""" % pending


    return context



def save_pending(action):

    set_pending_action(
        action
    )



def clear_pending():

    clear_pending_action()

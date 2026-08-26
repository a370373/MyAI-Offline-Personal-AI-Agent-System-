from core.memory_dispatcher import save_by_memory_type
from core.memory_importance import evaluate_memory
from context_manager import add_message



def process_memory(role, content):

    # 防止 AI 自己的回答污染記憶
    if role == "assistant":
        return {
            "saved": False,
            "type": "none",
            "reason": "assistant response not stored"
        }



    importance = evaluate_memory(
        content
    )


    # 不重要記憶

    if not importance.get(
        "save"
    ):

        add_message(
            role,
            content
        )


        return {
            "saved": False,
            "type": "short_term",
            "reason": importance.get(
                "reason",
                ""
            )
        }



    # 重要記憶

    result = save_by_memory_type(
        content
    )


    memory_type = result.get(
        "type"
    )



    # 短期上下文

    if memory_type == "short_term":

        # 不保存 AI 最終回答，避免錯誤回答污染短期記憶
        if role == "assistant":
            return {
                "saved": False,
                "type": "short_term",
                "reason": "skip assistant response"
            }


        add_message(
            role,
            content
        )



    return result

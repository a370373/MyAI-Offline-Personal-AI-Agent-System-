from core.memory_router import analyze_memory_type
from memory import save_memory, load_memory



def save_by_memory_type(text):

    result = analyze_memory_type(
        text
    )


    memory_type = result.get(
        "type"
    )



    # ------------------
    # 長期記憶
    # ------------------

    if memory_type == "long_term":

        data = load_memory(
            "long_term.json"
        )


        if not isinstance(data, list):

            data = []


        for item in data:

            if item.get(
                "content"
            ) == text:

                return {
                    "saved": False,
                    "type": "long_term",
                    "reason": "已存在"
                }



        data.append(
            {
                "content": text,
                "protected": True,
                "source": "user"
            }
        )


        save_memory(
            "long_term.json",
            data
        )


        return {
            "saved": True,
            "type": "long_term"
        }



    # ------------------
    # 近期記憶
    # ------------------

    if memory_type == "recent":

        data = load_memory(
            "recent.json"
        )


        if not isinstance(data, list):

            data = []



        # 專案/工作狀態只保留最新

        if data:

            data[-1] = {
                "content": text
            }

        else:

            data.append(
                {
                    "content": text
                }
            )



        save_memory(
            "recent.json",
            data
        )


        return {
            "saved": True,
            "type": "recent"
        }



    # ------------------
    # 知識庫
    # ------------------

    if memory_type == "knowledge":

        return {
            "saved": False,
            "type": "knowledge",
            "reason": "交由 knowledge_manager 管理"
        }



    return {
        "saved": False,
        "type": "short_term",
        "reason": "由 context_manager 管理"
    }

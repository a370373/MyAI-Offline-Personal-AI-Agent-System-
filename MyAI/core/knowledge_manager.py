from core.tool_manager import run_tool


KEYWORDS = [
    "專案",
    "架構",
    "檔案",
    "工具",
    "程式",
    "哪個",
    "負責",
    "位置",
    "結構"
]


def need_knowledge(text):

    for k in KEYWORDS:

        if k in text:
            return True

    return False



def get_knowledge(text):

    if not need_knowledge(text):

        return ""


    result = run_tool(
        {
            "tool":"knowledge_search",
            "keyword":text
        }
    )


    if not result.get("success"):

        return ""


    return f"""

相關專案知識：

{result.get("data")}

"""

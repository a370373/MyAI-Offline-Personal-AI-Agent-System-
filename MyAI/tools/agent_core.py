from model import ask
from tool_parser import parse_tool
from tool_manager import run_tool
from permission import check
from config import SYSTEM_PROMPT


def handle(user_input):

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": user_input
        }

    ]


    response = ask(messages)


    tool_request = parse_tool(response)


    if not tool_request:

        return response


    tool = tool_request["tool"]
    args = tool_request.get("args")


    if not check(tool):

        return "工具權限不足"


    result = run_tool(
        tool,
        args
    )


    final_messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content": f"""
使用者問題：

{user_input}


工具結果：

{result}


請整理後回答使用者。
不要輸出工具格式。
"""
        }

    ]


    return ask(final_messages)

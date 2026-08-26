def parse_tool(text):

    tools = [
        "system_info",
        "file_manager",
        "current_time",
        "shell"
    ]


    if "<tool>" in text and "</tool>" in text:

        data = text.split("<tool>")[1]
        data = data.split("</tool>")[0]

        lines = data.strip().split("\n")

        tool = lines[0].strip()

        if tool in tools:

            args = None

            if len(lines) > 1:
                args = "\n".join(lines[1:]).strip()

            return {
                "tool": tool,
                "args": args
            }


    # 容錯：小模型可能不照格式
    for tool in tools:

        if tool in text:

            return {
                "tool": tool,
                "args": None
            }


    return None

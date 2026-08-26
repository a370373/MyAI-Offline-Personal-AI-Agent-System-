from core.tool_registry import list_tools


def get_capabilities():
    tools = list_tools()

    result = []

    for tool in tools:
        result.append({
            "name": tool.get("name"),
            "description": tool.get(
                "description",
                ""
            )
        })

    return result


def has_capability(tool_name):
    tools = list_tools()

    for tool in tools:
        if tool.get("name") == tool_name:
            return True

    return False


def format_capabilities():
    caps = get_capabilities()

    text = "目前能力：\n"

    for item in caps:
        text += (
            f"- {item['name']}: "
            f"{item['description']}\n"
        )

    return text

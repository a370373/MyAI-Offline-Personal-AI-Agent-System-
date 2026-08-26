SAFE_TOOLS = [
    "system_info",
    "file_manager",
    "current_time",
    "shell"
]


def check(tool):

    return tool in SAFE_TOOLS

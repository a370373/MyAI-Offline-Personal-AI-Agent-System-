import importlib


TOOLS = {

    "system_info":
        "tools.system_info",

    "file_manager":
        "tools.file_manager",

    "current_time":
        "tools.time_tool",

    "shell":
        "tools.shell_tool"

}


def run_tool(name, args=None):

    if name not in TOOLS:
        return "工具不存在"


    module = importlib.import_module(
        TOOLS[name]
    )


    if args:
        return module.run(args)


    return module.run()


def list_tools():

    return list(TOOLS.keys())

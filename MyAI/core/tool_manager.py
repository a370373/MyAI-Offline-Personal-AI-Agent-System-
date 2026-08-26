import importlib

from core.tool_registry import get_tool
from core.tool_result import success, failure



def run_tool(action):


    # 舊格式相容
    if isinstance(action, str):

        name = action
        params = {}


    # JSON 格式
    elif isinstance(action, dict):

        name = action.get(
            "tool"
        )

        params = action


    else:

        return failure(
            "unknown",
            "parse",
            "工具格式錯誤"
        )



    if not name:

        return failure(
            "unknown",
            "parse",
            "缺少工具名稱"
        )



    tool_info = get_tool(
        name
    )


    if not tool_info:

        return failure(
            name,
            "load",
            "工具不存在"
        )



    module_path = tool_info.get(
        "module"
    )



    try:

        module = importlib.import_module(
            module_path
        )



        # ----------------
        # Shell
        # ----------------

        if name == "shell":

            command = params.get(
                "command"
            )


            if not command:

                return failure(
                    name,
                    "execute",
                    "缺少 shell 指令"
                )


            result = module.run(
                command
            )


            return success(
                name,
                "shell",
                result
            )



        # ----------------
        # File Manager
        # ----------------

        if name == "file_manager":

            action_type = params.get(
                "action",
                "list"
            )


            path = params.get(
                "path",
                "~"
            )


            if action_type == "tree":

                return module.tree(
                    path
                )


            elif action_type == "list":

                return module.list_dir(
                    path
                )


            elif action_type == "read":

                return module.read(
                    path
                )


            elif action_type == "search":

                return module.search(
                    path,
                    params.get(
                        "keyword",
                        ""
                    )
                )


            else:

                return failure(
                    name,
                    action_type,
                    "未知 file_manager 操作"
                )



        # ----------------
        # 一般工具
        # 支援參數傳入
        # ----------------

        try:

            result = module.run(
                **params
            )


        except TypeError:

            result = module.run()



        return success(
            name,
            "run",
            result
        )



    except Exception as e:

        return failure(
            name,
            "execute",
            str(e)
        )

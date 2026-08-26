import json
import importlib


class Agent:

    def __init__(self):
        self.tools = self.load_tools()


    def load_tools(self):

        with open(
            "tools/registry.json",
            "r"
        ) as f:
            data = json.load(f)

        return data["tools"]


    def show_tools(self):

        for tool in self.tools:
            print(
                tool["name"],
                "-",
                tool["description"]
            )


    def use_tool(
        self,
        name,
        *args,
        **kwargs
    ):

        tool = None

        for t in self.tools:
            if t["name"] == name:
                tool = t
                break


        if not tool:
            return {
                "error":
                "tool not found"
            }


        module = importlib.import_module(
            tool["module"]
        )


        if hasattr(
            module,
            "run"
        ):
            return module.run(
                *args,
                **kwargs
            )

        return {
            "error":
            "tool has no run()"
        }

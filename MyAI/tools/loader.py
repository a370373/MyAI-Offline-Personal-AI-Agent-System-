import json
import importlib


def load_tools():

    with open(
        "tools/registry.json",
        "r"
    ) as f:

        data = json.load(f)


    tools = {}


    for name, config in data.items():

        module = importlib.import_module(
            config["module"]
        )

        tools[name] = {
            "module": module,
            "description": config["description"]
        }


    return tools

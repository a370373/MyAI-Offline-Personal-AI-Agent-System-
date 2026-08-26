import json
from pathlib import Path

from tools.browser_tool import browser_read
from tools.browser_controller import browser


ROOT = Path(__file__).parent.parent
REGISTRY = ROOT / "tools" / "registry.json"


def load_tools():
    with open(REGISTRY, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data["tools"]


def get_tool(name):
    tools = load_tools()

    for tool in tools:
        if tool.get("name") == name:
            return tool

    return None


def list_tools():
    return load_tools()

import json

targets = [
    "context.json",
    "data/short_context.json",
    "memory/short_term/context.json"
]

for path in targets:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "messages" in data:
            data["messages"] = []

        if "pending_action" in data:
            data["pending_action"] = None

        if path == "data/short_context.json":
            data = {}

        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )

        print("清理完成:", path)

    except Exception as e:
        print("跳過:", path, e)


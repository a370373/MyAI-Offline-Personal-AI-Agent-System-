from tools.loader import load_tools


tools = load_tools()


print("MyAI Available Tools:")


for name, info in tools.items():

    print(
        "-",
        name,
        ":",
        info["description"]
    )

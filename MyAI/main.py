from core.agent_core import handle
from core.runtime.runtime_manager import RuntimeManager

runtime_manager = RuntimeManager()


print("MyAI Agent 啟動")


while True:

    user = input("\n你：")

    if user == "exit":
        break

    answer = handle(user, runtime_manager)

    print("\nAI：")
    print(answer)

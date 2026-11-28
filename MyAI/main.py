from core.agent_core import handle
from core.goal_controller import run_goal
from core.runtime.runtime_manager import RuntimeManager

runtime_manager = RuntimeManager()


print("MyAI Agent 啟動")


while True:

    user = input("\n你：")

    if user == "exit":
        break

    if (
        user.strip() == '/goal'
        or user.strip().startswith('/goal ')
    ):
        goal = user.strip()[len('/goal'):].strip()
        answer = run_goal(goal, runtime_manager)
    else:
        answer = handle(user, runtime_manager)
    print("\nAI：")
    print(answer)

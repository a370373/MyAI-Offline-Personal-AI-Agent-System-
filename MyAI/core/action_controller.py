from core.tool_manager import run_tool
from core.action_executor import ActionExecutor

MAX_ACTIONS = 10


def execute_actions(actions, browser=None):

    print("[DEBUG execute_actions input]", actions)

    results = []

    executor = None

    if browser:
        executor = ActionExecutor(browser)


    count = 0


    for item in actions:

        if count >= MAX_ACTIONS:
            break


        # browser action
        if (
            isinstance(item, dict)
            and item.get("tool") == "browser"
            and "action" in item
        ):

            if executor:
                result = executor.execute(item)
            else:
                result = {
                    "success": False,
                    "error": "no browser executor"
                }

            results.append(result)

            count += 1

            continue


        # old wrapper format
        if (
            isinstance(item, dict)
            and item.get("tool") == "browser"
            and "actions" in item
        ):

            for action in item["actions"]:

                if executor:
                    result = executor.execute(action)
                else:
                    result = {
                        "success": False
                    }

                results.append(result)

                count += 1


            continue


        # normal tool
        result = run_tool(item)

        results.append(result)

        count += 1


    print("[DEBUG execute_actions output]", results)

    return results

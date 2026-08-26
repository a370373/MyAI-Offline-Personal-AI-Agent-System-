VALID_ACTIONS = [
    "open",
    "click",
    "type",
    "read",
    "wait",
    "done"
]


def validate_action(action):

    if not isinstance(action, dict):
        return {
            "action":"wait"
        }


    name = action.get("action")


    if name not in VALID_ACTIONS:
        return {
            "action":"wait"
        }


    return action

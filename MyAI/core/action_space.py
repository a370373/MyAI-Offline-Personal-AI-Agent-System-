ACTIONS = [
    "open",
    "read",
    "find",
    "click",
    "click_element",
    "type",
    "press_enter",
    "wait",
    "scroll",
    "back"
]


def valid_action(action):
    return action in ACTIONS

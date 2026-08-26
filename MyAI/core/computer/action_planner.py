def create_action(target):

    if target.startswith("http"):
        return {
            "action": "open",
            "url": target
        }


    actions = {

        "search_box": {
            "action": "click",
            "x": 500,
            "y": 300
        },

        "search_button": {
            "action": "click",
            "x": 700,
            "y": 300
        }

    }


    return actions.get(
        target,
        None
    )


def adapt(tasks):

    actions = []


    for t in tasks:

        intent = t.get(
            "intent"
        )


        if intent == "open_url":

            actions.append(
                {
                    "tool":"browser",
                    "action":"open",
                    "url":t.get("url")
                }
            )


        elif intent == "find_element":

            actions.append(
                {
                    "tool":"browser",
                    "action":"find",
                    "target":t.get("target")
                }
            )


        elif intent == "click_element":

            actions.append(
                {
                    "tool":"browser",
                    "action":"click",
                    "target":t.get("target")
                }
            )


        elif intent == "input_text":

            actions.append(
                {
                    "tool":"browser",
                    "action":"type",
                    "target":t.get("target"),
                    "text":t.get("text")
                }
            )


        elif intent == "submit":

            actions.append(
                {
                    "tool":"browser",
                    "action":"submit"
                }
            )


    return actions

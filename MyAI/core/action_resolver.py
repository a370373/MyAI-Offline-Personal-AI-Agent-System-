from core.element_selector import ElementSelector


class ActionResolver:


    def __init__(self, finder):

        self.selector = ElementSelector(
            finder
        )


    def resolve(self, action):

        if not isinstance(action, dict):
            return action


        name = action.get(
            "action"
        )


        if name == "click_element":

            target = action.get(
                "target",
                ""
            )


            element = self.selector.best(
                target
            )


            if element:

                return {
                    "action":"click",
                    "x":element.get("x"),
                    "y":element.get("y")
                }


        if name == "type":

            return {
                "action":"type",
                "text":action.get(
                    "text",
                    ""
                )
            }


        return action

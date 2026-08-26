class TargetResolver:


    def __init__(self, selector):

        self.selector = selector



    def resolve(self, action):

        if not isinstance(action, dict):
            return action


        act = action.get(
            "action",
            ""
        )


        if act != "click":
            return action


        if action.get("x") is not None:
            return action


        target = action.get(
            "target",
            ""
        )


        if not target:
            return action



        element = self.selector.best(
            target
        )


        if not element:

            return {
                "action":"stop",
                "reason":"target not found"
            }



        return {

            "action":"click",

            "x":
            element.get("x"),

            "y":
            element.get("y"),

            "target":
            target

        }

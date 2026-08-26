class ActionPlanner:


    def plan(self, goal, state):

        actions = []


        next_action = state.get(
            "next_action"
        )


        if not next_action:
            return actions



        action = next_action.get(
            "action"
        )



        if action == "find_input":

            actions.append(
                {
                    "action":"type",
                    "element":next_action.get(
                        "target",
                        ""
                    ),
                    "text":goal
                }
            )


            actions.append(
                {
                    "action":"press_enter"
                }
            )



        elif action == "analyze_more":

            actions.append(
                {
                    "action":"analyze_dom"
                }
            )



        return actions

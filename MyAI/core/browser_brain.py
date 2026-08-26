class BrowserBrain:


    def analyze(self, dom, goal):

        state = {
            "goal": goal,
            "page_type": "unknown",
            "next_action": None
        }


        text = str(dom).lower()


        if (
            "search" in text
            or "搜尋" in text
            or "q" in text
        ):

            state["page_type"] = "search_page"

            state["next_action"] = {
                "action":"find_input",
                "target":"搜尋"
            }


        elif (
            "password" in text
            or "密碼" in text
        ):

            state["page_type"] = "login_page"

            state["next_action"] = {
                "action":"find_input",
                "target":"帳號"
            }


        else:

            state["next_action"] = {
                "action":"analyze_more"
            }


        return state

class TaskPlanner:


    def plan(self, intent):

        tasks = []


        if not intent:
            return tasks



        if intent.get("action") == "open":

            tasks = [

                {
                    "action":"open",
                    "url":
                    intent.get("url")
                },

                {
                    "action":"wait",
                    "seconds":2
                },

                {
                    "action":"analyze_dom"
                }

            ]



        elif intent.get("intent") == "search":


            tasks = [

                {
                    "action":"open",
                    "url":
                    "https://www.google.com"
                },

                {
                    "action":"wait",
                    "seconds":2
                },

                {
                    "action":"find_element",
                    "target":"搜尋"
                },

                {
                    "action":"click_element"
                },

                {
                    "action":"type",
                    "target":"搜尋",
                    "text":
                    intent.get(
                        "query",
                        ""
                    )
                },

                {
                    "action":"submit"
                }

            ]


        return tasks

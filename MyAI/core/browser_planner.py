class BrowserPlanner:

    def plan(self, goal):

        steps = []

        goal_lower = goal.lower()


        # 搜尋任務
        if "搜尋" in goal or "search" in goal:

            keyword = goal

            for word in [
                "搜尋",
                "search",
                "查詢",
                "查一下"
            ]:
                keyword = keyword.replace(
                    word,
                    ""
                )


            steps.append(
                {
                    "tool":"browser",
                    "command":"find_input",
                    "keyword":"搜尋"
                }
            )


            steps.append(
                {
                    "tool":"browser",
                    "command":"type",
                    "text":keyword.strip()
                }
            )


            steps.append(
                {
                    "tool":"browser",
                    "command":"submit"
                }
            )


        # 登入流程
        elif "登入" in goal:

            steps.append(
                {
                    "tool":"browser",
                    "command":"find_input",
                    "keyword":"帳號"
                }
            )


            steps.append(
                {
                    "tool":"browser",
                    "command":"find_input",
                    "keyword":"密碼"
                }
            )


        else:

            steps.append(
                {
                    "tool":"browser",
                    "command":"analyze_dom"
                }
            )


        return steps

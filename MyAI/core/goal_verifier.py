class GoalVerifier:


    def verify(
        self,
        goal,
        history,
        result,
        dom
    ):

        goal=goal.lower()


        text=str(dom).lower()


        # 搜尋任務

        if "搜尋" in goal or "search" in goal:

            if "result" in text or "google" in text:

                if history:

                    last=history[-1]

                    if last["action"].get("action")=="type":

                        return True



        # 開啟網站

        if "open" in goal:

            if result.get("success"):

                return True



        return False

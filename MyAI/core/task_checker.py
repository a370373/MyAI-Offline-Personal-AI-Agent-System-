
class TaskChecker:



    def check(
        self,
        goal,
        result
    ):


        goal=str(goal)

        data=str(result)



        # Google 搜尋類

        if (
            "搜尋" in goal
            or
            "search" in goal.lower()
        ):


            if (
                "google" in data.lower()
                and
                (
                    "result"
                    in data.lower()

                    or

                    "搜尋"
                    in data
                )
            ):

                return True




        # 開網站

        if "打開" in goal:


            if (
                "success"
                in data.lower()
            ):

                return True




        # 輸入完成

        if (
            "輸入"
            in goal
        ):


            if (
                "text"
                in data
                and
                "success"
                in data.lower()
            ):

                return True




        return False


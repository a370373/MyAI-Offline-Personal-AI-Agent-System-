class IntentRouter:


    def clean_query(self, task):

        remove_words = [
            "打開",
            "開啟",
            "搜尋",
            "search",
            "google",
            "Google"
        ]


        for word in remove_words:

            task = task.replace(
                word,
                ""
            )


        return " ".join(
            task.split()
        )



    def route(self, task):

        raw = task


        task_lower = task.lower()


        if (
            "搜尋" in raw
            or
            "search" in task_lower
        ):

            return {
                "intent":"search",
                "query":self.clean_query(raw)
            }



        if (
            "打開" in raw
            or
            "開啟" in raw
            or
            "open" in task_lower
        ):

            return {
                "intent":"open",
                "query":self.clean_query(raw)
            }



        return {
            "intent":"unknown",
            "query":raw
        }

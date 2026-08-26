class BrowserFeedbackLoop:

    MAX_RETRY = 3


    def __init__(
        self,
        browser,
        brain,
        planner,
        executor,
        feedback
    ):
        self.browser = browser
        self.brain = brain
        self.planner = planner
        self.executor = executor
        self.feedback = feedback



    def run(self, goal):

        for attempt in range(
            self.MAX_RETRY
        ):

            print(
                f"[Agent Loop] attempt {attempt+1}"
            )


            # 讀 DOM

            dom = self.browser.understand()


            # Brain 分析

            state = self.brain.analyze(
                dom,
                goal
            )


            print(
                "[Brain]",
                state
            )


            # Planner

            actions = self.planner.plan(
                goal,
                state
            )


            print(
                "[Plan]",
                actions
            )


            # 執行

            result = self.executor.execute(
                actions
            )


            print(
                "[Result]",
                result
            )


            # 回饋判斷

            check = self.feedback.check(
                actions,
                result,
                self.browser
            )


            if check.get(
                "success"
            ):

                return {
                    "success":True,
                    "result":result
                }


            print(
                "[Repair]",
                check
            )



        return {
            "success":False,
            "error":"retry failed"
        }

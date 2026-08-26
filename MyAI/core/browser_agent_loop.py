
class BrowserAgentLoop:

    MAX_RETRY = 3

    def __init__(self, browser, brain, planner, executor):
        self.browser = browser
        self.brain = brain
        self.planner = planner
        self.executor = executor


    def run(self, goal):

        for i in range(self.MAX_RETRY):

            print("[Browser Loop] analyze", i+1)

            dom = self.browser.understand()

            state = self.brain.analyze(
                dom,
                goal
            )

            actions = self.planner.plan(
                goal,
                state
            )

            result = self.executor.execute(
                actions
            )


            if self.success(result):

                return {
                    "success": True,
                    "result": result
                }


            print(
                "[Browser Loop] retry"
            )


        return {
            "success":False,
            "error":"failed"
        }



    def success(self,result):

        if not result:
            return False

        if isinstance(result,list):

            for r in result:

                if isinstance(r,dict):

                    if r.get("success") is False:
                        return False


        return True

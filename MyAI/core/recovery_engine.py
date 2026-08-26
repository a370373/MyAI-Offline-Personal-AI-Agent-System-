import time


class RecoveryEngine:


    def __init__(self, agent=None):

        self.agent = agent

        self.retry_count = 0

        self.max_retry = 3



    def should_retry(
        self,
        result
    ):

        if not isinstance(result, dict):
            return False


        return result.get(
            "success"
        ) == False



    def recover(
        self,
        result
    ):


        self.retry_count += 1


        print(
            "[RECOVERY START]",
            self.retry_count
        )


        if self.retry_count > self.max_retry:

            print(
                "[RECOVERY STOP]"
            )

            return False



        error=result.get(
            "error",
            ""
        )


        print(
            "[ERROR]",
            error
        )


        # 重新讀 DOM

        try:

            if self.agent:


                dom=self.agent.browser_agent.understand()


                print(
                    "[RECOVERY DOM RELOAD]"
                )


                simple=self.agent.simplify_dom(
                    dom
                )


                self.agent.last_dom=simple



                print(
                    "[RECOVERY DOM UPDATED]"
                )


        except Exception as e:

            print(
                "[DOM RELOAD ERROR]",
                e
            )



        # 等待頁面穩定

        time.sleep(1)



        return True



    def reset(self):

        self.retry_count=0

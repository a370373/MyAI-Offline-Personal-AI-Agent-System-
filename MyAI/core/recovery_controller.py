class RecoveryController:


    def __init__(
        self,
        browser_agent,
        dom_memory
    ):

        self.browser_agent = browser_agent

        self.dom_memory = dom_memory



    def reload_dom(self):

        try:

            dom=self.browser_agent.understand()


            self.dom_memory.store(
                dom
            )


            print(
                "[RECOVERY] DOM refreshed"
            )


            return dom


        except Exception as e:

            print(
                "[RECOVERY DOM ERROR]",
                e
            )

            return None



    def recover(
        self,
        result
    ):


        if not isinstance(
            result,
            dict
        ):

            return False



        if result.get(
            "success"
        ):

            return False



        print(
            "[RECOVERY START]"
        )


        self.reload_dom()


        return True

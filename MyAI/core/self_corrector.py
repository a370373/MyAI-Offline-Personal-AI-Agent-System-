class SelfCorrector:


    def __init__(self, browser=None):

        self.browser = browser



    def analyze(
        self,
        action,
        result
    ):


        if isinstance(result, str):

            return {
                "status":"success",
                "retry":False
            }


        if isinstance(result, str):

            return {
                "status":"success",
                "retry":False
            }


        if result.get("success"):

            return {
                "status":"success",
                "retry":False
            }



        error = str(
            result.get(
                "error",
                ""
            )
        )


        print(
            "[SelfCorrector]",
            error
        )



        if (
            "not found" in error
            or
            "element" in error
        ):


            target = action.get(
                "target",
                ""
            )


            candidates = []


            if self.browser:

                try:

                    dom = self.browser.analyze()

                    dom_text = str(dom)


                    for x in [
                        "textarea",
                        "input",
                        "button"
                    ]:

                        if x in dom_text:

                            candidates.append(x)


                except Exception:

                    pass



            candidates += [
                target,
                "輸入框",
                "聊天輸入",
                "textbox",
                "message"
            ]



            return {

                "status":"failed",

                "retry":True,

                "new_actions":[

                    {
                        "intent":
                        "find_element",

                        "target":x

                    }

                    for x in candidates

                ]

            }



        if "timeout" in error:


            return {

                "status":"failed",

                "retry":True,

                "new_actions":[

                    {
                        "intent":"wait",
                        "seconds":3
                    },

                    action

                ]

            }



        return {

            "status":"failed",

            "retry":False,

            "reason":error

        }

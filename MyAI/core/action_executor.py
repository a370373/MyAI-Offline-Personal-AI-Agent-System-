class ActionExecutor:

    def __init__(self, browser):

        self.browser = browser
        self.last_element = None



    def execute(self, action):

        action_type = action.get(
            "action"
        )

        # 支援 TaskExtractor intent 格式
        if not action_type:
            intent = action.get(
                "intent"
            )

            mapping = {
                "open_url": "open",
                "find_element": "find_element",
                "click_element": "click_element",
                "input_text": "type",
                "submit": "submit"
            }

            action_type = mapping.get(
                intent
            )

            action["action"] = action_type


        # 開網站
        if action_type == "open":

            return self.browser.open(
                action.get("url")
            )


        # 等待
        if action_type == "wait":

            import time

            time.sleep(
                action.get(
                    "seconds",
                    1
                )
            )

            return {
                "success": True,
                "action": "wait"
            }



        # DOM 找元素
        if action_type in ("find_element", "find"):

            element = self.browser.find(
                action.get(
                    "target"
                )
            )


            if not element:

                return {
                    "success": False,
                    "error":
                    "element not found"
                }


            self.last_element = element


            return {
                "success": True,
                "action":
                "find_element",
                "element":
                element
            }



        # 點擊元素
        if action_type in ("click_element", "click"):


            element = (
                action.get("element")
                or self.last_element
            )


            if not element:

                return {
                    "success": False,
                    "error":
                    "missing element"
                }


            return self.browser.click(
                element
            )



        # 輸入
        if action_type == "type":

            return self.browser.type(
                action.get(
                    "target",
                    "搜尋"
                ),
                action.get(
                    "text",
                    ""
                )
            )



        # 送出
        if action_type == "submit":

            return self.browser.submit()



        # DOM 分析

        if action_type == "analyze_dom":

            return self.browser.analyze()



        return {
            "success": False,
            "error":
            "unknown action: "
            + str(action_type)
        }

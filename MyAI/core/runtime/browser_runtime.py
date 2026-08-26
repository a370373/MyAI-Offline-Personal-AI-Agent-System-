class BrowserRuntime:


    def __init__(self, browser_agent):

        self.agent = browser_agent


    def open(self,url):

        return self.agent.browser.navigate(
            url
        )


    def navigate(self, url):
        return self.open(url)

    def analyze(self):

        return self.agent.analyze()


    def find(self, keyword):

        try:
            self.prepare()
        except Exception:
            pass


        return self.agent.find_best(
            keyword
        )


    def type(self, keyword, text):

        element = self.find(
            keyword
        )

        if not element:

            return {
                "success":False,
                "error":"input not found"
            }


        try:

            self.agent.finder.page.click(
                element["x"],
                element["y"]
            )


            self.agent.finder.page.type_text(
                text
            )


            return {
                "success":True,
                "action":"type",
                "text":text
            }


        except Exception as e:

            return {
                "success":False,
                "error":str(e)
            }


    def submit(self):

        try:

            result = self.agent.finder.page.press_enter()

            return {
                "success": True,
                "action": "submit",
                "result": result
            }

        except Exception as e:

            return {
                "success": False,
                "action": "submit",
                "error": str(e)
            }


    def click(self,target):

        # 支援直接傳入 DOM element
        if isinstance(target, dict):
            element = target

        else:
            element = self.agent.find_best(
                target
            )

        if not element:

            return {
                "success":False,
                "error":"element not found"
            }

        return self.agent.finder.page.click(
            element["x"],
            element["y"]
        )

    def scroll(self,direction="down"):

        distance = 800


        if direction == "up":
            distance = -800


        return self.agent.finder.page.scroll(
            distance
        )


    def back(self):

        return self.agent.finder.page.back()


    def refresh(self):

        return self.agent.finder.page.refresh()


    def screenshot(self):

        return self.agent.finder.page.screenshot()


    def wait_response(self):
        try:
            return True
        except Exception:
            return False


    def analyze(self):
        try:
            return self.agent.analyze()
        except Exception as e:
            return {
                "error": str(e)
            }


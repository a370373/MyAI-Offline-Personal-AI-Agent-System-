class BrowserRuntime:

    def get_html(self):
        return self.agent.browser.get_html()



    def __init__(self, browser_agent):

        self.agent = browser_agent

        self.waiter = browser_agent.waiter
        self.frames = browser_agent.frames
        self.scroll = browser_agent.scroll
        self.spa = browser_agent.spa


    def prepare(self):

        try:
            captcha = self.agent.captcha.detect(
                self.agent.understand()
            )

            if captcha.get("captcha"):

                return self.agent.human.request(
                    captcha["reason"]
                )

        except Exception:
            pass


        try:
            self.waiter.wait(
                self.agent.page
            )
        except Exception:
            pass


        try:
            self.spa.detect(
                self.agent.page
            )
        except Exception:
            pass


        try:
            self.frames.detect(
                self.agent.page
            )
        except Exception:
            pass


        return True



    def open(self, url):

        self.prepare()

        return self.agent.browser.navigate(
            url
        )


    def find(self, keyword):

        self.prepare()


        element = self.agent.find_best(
            keyword
        )


        if element:

            try:
                self.scroll.ensure_visible(
                    self.agent.page,
                    element
                )
            except Exception:
                pass


        return element



    def type(self, keyword, text):

        element = self.find(
            keyword
        )


        if not element:

            return {
                "success":False,
                "error":"element not found"
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



    def click(self, keyword):

        element=self.find(
            keyword
        )


        if not element:

            return {
                "success":False,
                "error":"element not found"
            }


        try:

            self.agent.finder.page.click(
                element["x"],
                element["y"]
            )


            return {
                "success":True,
                "action":"click"
            }


        except Exception as e:

            return {
                "success":False,
                "error":str(e)
            }

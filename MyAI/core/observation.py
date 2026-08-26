class Observation:

    def __init__(self, browser=None):

        self.browser = browser



    def observe(self):

        if not self.browser:

            return {
                "success": False,
                "error": "browser unavailable"
            }


        try:

            dom = self.browser.analyze()


            return {
                "success": True,
                "dom": dom
            }


        except Exception as e:


            return {
                "success": False,
                "error": str(e)
            }

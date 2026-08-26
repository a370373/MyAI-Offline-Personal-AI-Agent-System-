class CookieManager:

    def __init__(self, browser):
        self.browser = browser


    def get_cookies(self):

        try:
            return self.browser.get_cookies()

        except Exception:

            return []


    def save(self):

        return self.get_cookies()


    def restore(self, cookies):

        try:

            self.browser.set_cookies(
                cookies
            )

            return True

        except Exception:

            return False

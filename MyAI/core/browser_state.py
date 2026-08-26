class BrowserState:

    def __init__(self):
        self.logged_in = False
        self.current_url = ""
        self.title = ""
        self.captcha_detected = False
        self.loading = False


    def update(self, page):

        try:
            self.current_url = page.url
            self.title = page.title()

        except:
            pass


    def detect_captcha(self, html):

        keys = [
            "captcha",
            "recaptcha",
            "hcaptcha",
            "verify you are human"
        ]

        html = html.lower()

        for k in keys:
            if k in html:
                self.captcha_detected = True
                return True

        return False

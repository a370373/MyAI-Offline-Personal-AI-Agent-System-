class CaptchaDetector:


    KEYWORDS = [
        "captcha",
        "驗證碼",
        "verify",
        "robot",
        "recaptcha",
        "challenge"
    ]


    def detect(self, dom):

        text=str(dom).lower()


        for word in self.KEYWORDS:

            if word in text:

                return {
                    "captcha":True,
                    "reason":word
                }


        return {
            "captcha":False
        }

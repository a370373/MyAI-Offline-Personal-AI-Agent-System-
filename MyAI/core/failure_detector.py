BLOCK_WORDS = [

    "unusual traffic",

    "not a robot",

    "captcha",

    "verify",

    "驗證",

    "異常流量",

    "robot"

]


def detect_failure(text):


    if not text:

        return {

            "blocked":False

        }



    lower=text.lower()



    for word in BLOCK_WORDS:

        if word.lower() in lower:

            return {

                "blocked":True,

                "reason":"anti_bot",

                "keyword":word

            }



    return {

        "blocked":False

    }

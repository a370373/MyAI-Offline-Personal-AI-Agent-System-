import time


class Recovery:


    def __init__(
        self,
        max_retry=3
    ):

        self.max_retry=max_retry



    def should_retry(
        self,
        result,
        retry_count
    ):


        if retry_count >= self.max_retry:
            return False


        if not isinstance(result,dict):
            return False


        if result.get(
            "success"
        ) is True:
            return False



        error=str(
            result.get(
                "error",
                ""
            )
        ).lower()



        retry_words=[

            "not found",

            "missing",

            "low confidence",

            "no element",

            "unknown action"

        ]



        for w in retry_words:

            if w in error:
                return True



        return False



    def wait(self):

        time.sleep(1)

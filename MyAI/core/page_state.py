import time


class PageState:


    def wait_ready(
        self,
        page,
        timeout=5
    ):

        for i in range(timeout):

            try:

                result=page.evaluate(
                    """
                    document.readyState
                    """
                )


                if result=="complete":

                    print(
                        "[PAGE READY]"
                    )

                    return True


            except:
                pass


            time.sleep(1)


        print(
            "[PAGE TIMEOUT]"
        )

        return False

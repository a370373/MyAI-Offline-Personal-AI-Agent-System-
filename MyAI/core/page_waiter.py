import time


class PageWaiter:


    def wait_loaded(
        self,
        page,
        timeout=10
    ):

        for i in range(timeout):

            try:

                state = page.evaluate(
                    """
                    document.readyState
                    """
                )

                if state=="complete":
                    return True

            except:
                pass

            time.sleep(1)


        return False

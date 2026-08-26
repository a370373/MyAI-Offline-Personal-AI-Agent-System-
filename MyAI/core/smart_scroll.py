import time


class SmartScroll:


    def search_down(
        self,
        page,
        keyword,
        times=5
    ):


        for i in range(times):

            element = page.find(keyword)

            if element:
                return element


            page.evaluate(
                """
                window.scrollBy(
                    0,
                    window.innerHeight
                )
                """
            )


            time.sleep(1)


        return None

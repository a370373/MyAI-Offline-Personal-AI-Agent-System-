
from time import sleep


class DOMObserver:

    def __init__(self, browser):

        self.browser = browser


    def snapshot(self):

        try:

            page = self.browser.finder.page

            html = page.content()

            return {

                "url": page.url,

                "title": page.title(),

                "html_length": len(html),

                "html": html[:30000]

            }


        except Exception as e:

            return {

                "error": str(e)

            }



    def diff(self,before,after):

        return {

            "changed":
                before.get("html_length")
                !=
                after.get("html_length"),


            "before":
                before.get("html_length",0),


            "after":
                after.get("html_length",0)

        }



    def observe(self):

        before = self.snapshot()

        sleep(1)

        after = self.snapshot()


        return {

            "before":before,

            "after":after,

            "diff":
                self.diff(
                    before,
                    after
                )

        }

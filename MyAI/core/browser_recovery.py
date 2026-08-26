import time


class BrowserRecovery:


    def __init__(self,finder):

        self.finder=finder



    def retry_find(
        self,
        keyword,
        retry=3
    ):

        for i in range(retry):

            element=self.finder.find_best(
                keyword
            )

            if element:

                return element


            time.sleep(1)


        return None




    def retry_input(
        self,
        keyword,
        text
    ):


        element=self.retry_find(
            keyword
        )


        if not element:

            return {

                "success":False,

                "error":"element missing"

            }



        try:

            self.finder.page.click(

                element["x"],

                element["y"]

            )


            self.finder.page.type_text(

                text

            )


            return {

                "success":True,

                "element":element

            }


        except Exception as e:


            return {

                "success":False,

                "error":str(e)

            }

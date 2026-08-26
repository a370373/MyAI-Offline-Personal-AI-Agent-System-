class GoogleAdapter:

    name="google"


    def match(self,url):

        return "google." in url



    def translate(self,intent):


        if intent=="search":

            return {
                "action":"find_and_type",
                "role":"searchbox"
            }


        return None

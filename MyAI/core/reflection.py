class Reflection:

    def check_result(self,result):

        if result is None:
            return {
                "success":False,
                "error":"empty result"
            }


        if isinstance(result,dict):

            if result.get("success") is False:
                return {
                    "success":False,
                    "error":result.get(
                        "error",
                        "unknown error"
                    )
                }


            return {
                "success":True,
                "error":None
            }


        return {
            "success":True,
            "error":None
        }



    def analyze_failure(self,result):

        error=result.get(
            "error",
            ""
        )


        if "no element" in error:

            return {
                "action":"reanalyze_dom"
            }


        if "timeout" in error:

            return {
                "action":"retry"
            }


        return {
            "action":"stop"
        }


def check_result(result):

    if not result:

        return {
            "success":False,
            "error":"empty result"
        }


    if isinstance(result,dict):

        return {
            "success":result.get(
                "success",
                True
            ),
            "error":result.get(
                "error"
            )
        }


    return {
        "success":True,
        "error":None
    }


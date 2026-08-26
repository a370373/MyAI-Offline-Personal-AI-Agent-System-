class BrowserFeedback:

    def check(self, action, result, browser_agent):

        if not result:
            return {
                "success": False,
                "reason": "no result"
            }


        if result.get("success") is False:
            return {
                "success": False,
                "reason": result.get(
                    "error",
                    "unknown"
                )
            }


        dom = browser_agent.understand()


        if action.get("action") in [
            "smart_type",
            "type"
        ]:

            if dom:
                return {
                    "success": True,
                    "reason": "input executed"
                }


        return {
            "success": True,
            "reason": "action completed"
        }

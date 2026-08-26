from core.risk_analyzer import analyze



def check_permission(action):


    risk = analyze(
        action
    )


    level = risk["level"]



    if level == "LOW":

        return {
            "allowed": True,
            "require_confirm": False,
            "reason": risk["reason"]
        }



    if level == "MEDIUM":

        return {
            "allowed": False,
            "require_confirm": True,
            "reason": risk["reason"]
        }



    if level == "HIGH":

        return {
            "allowed": False,
            "require_confirm": True,
            "blocked": True,
            "reason": risk["reason"]
        }

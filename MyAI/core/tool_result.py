def success(tool, action, data):

    return {
        "success": True,
        "tool": tool,
        "action": action,
        "data": data,
        "error": None
    }



def failure(tool, action, error):

    return {
        "success": False,
        "tool": tool,
        "action": action,
        "data": None,
        "error": error
    }

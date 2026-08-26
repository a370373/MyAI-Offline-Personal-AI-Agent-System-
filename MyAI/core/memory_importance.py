def evaluate_memory(text):

    text = text.strip()


    # 明確要求記住

    if any(
        word in text
        for word in [
            "記住",
            "記得",
            "請保存",
            "不要忘記"
        ]
    ):

        return {
            "save": True,
            "type": "long_term",
            "protected": True,
            "reason": "使用者明確要求記憶"
        }



    # 個人偏好

    if any(
        word in text
        for word in [
            "我喜歡",
            "我的習慣",
            "偏好",
            "習慣"
        ]
    ):

        return {
            "save": True,
            "type": "long_term",
            "protected": True,
            "reason": "使用者偏好"
        }



    # 工作狀態

    if any(
        word in text
        for word in [
            "正在",
            "目前",
            "正在修改",
            "正在開發"
        ]
    ):

        return {
            "save": True,
            "type": "recent",
            "protected": False,
            "reason": "近期狀態"
        }



    # 一般聊天不保存

    return {
        "save": False,
        "type": "none",
        "protected": False,
        "reason": "普通對話"
    }

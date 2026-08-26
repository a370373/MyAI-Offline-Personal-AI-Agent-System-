def analyze_memory_type(text):

    text = text.strip()



    # -------------------
    # 長期記憶
    # -------------------

    long_term_words = [
        "記住",
        "請記得",
        "以後都",
        "永遠",
        "我的偏好",
        "設定"
    ]


    for word in long_term_words:

        if word in text:

            return {
                "type": "long_term",
                "allow_update": True,
                "reason": "使用者明確要求記憶"
            }




    # -------------------
    # 近期狀態
    # -------------------

    recent_words = [
        "目前",
        "最近",
        "正在",
        "這次",
        "現在"
    ]


    for word in recent_words:

        if word in text:

            return {
                "type": "recent",
                "allow_update": True,
                "reason": "近期工作狀態"
            }





    # -------------------
    # 專案知識
    # -------------------

    knowledge_words = [
        "架構",
        "設計",
        "規格",
        "文件",
        "分析"
    ]


    for word in knowledge_words:

        if word in text:

            return {
                "type": "knowledge",
                "allow_update": False,
                "reason": "專案知識"
            }




    return {
        "type": "short_term",
        "allow_update": True,
        "reason": "一般對話"
    }

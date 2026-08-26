
def normalize_keyword(text):

    replace={
        "搜尋":"search",
        "登入":"login",
        "登錄":"login",
        "下載":"download",
        "播放":"play"
    }


    return replace.get(
        text,
        text
    )



def fallback_keywords(keyword):

    k=normalize_keyword(keyword)


    return [
        keyword,
        k,
        keyword.lower()
    ]


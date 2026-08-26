KEYWORDS = {

    "搜尋": [
        "search",
        "搜尋",
        "query",
        "q"
    ],

    "登入": [
        "login",
        "登入",
        "sign"
    ],

    "下一步": [
        "next",
        "下一步",
        "continue"
    ],

    "播放": [
        "play",
        "播放"
    ],

    "下載": [
        "download",
        "下載"
    ]

}



def score_element(element, intent):

    score = 0


    text = " ".join([
        str(element.get("text","")),
        str(element.get("placeholder","")),
        str(element.get("id","")),
        str(element.get("name","")),
        str(element.get("type",""))
    ]).lower()


    keywords = KEYWORDS.get(
        intent,
        [intent]
    )


    for word in keywords:

        if word.lower() in text:

            score += 20



    tag = element.get(
        "tag",
        ""
    ).lower()


    if tag == "input":

        score += 10


    if tag == "button":

        score += 8


    if tag == "a":

        score += 5


    return score




def rank_elements(elements, intent, limit=10):


    ranked=[]


    for e in elements:

        ranked.append(
            (
                score_element(
                    e,
                    intent
                ),
                e
            )
        )


    ranked.sort(
        key=lambda x:x[0],
        reverse=True
    )


    return [
        {
            "score":score,
            "element":element
        }

        for score,element in ranked[:limit]
    ]

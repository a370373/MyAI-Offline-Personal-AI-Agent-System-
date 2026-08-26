import json
import os


KNOWLEDGE_PATH = "knowledge/user/project.json"


def search(keyword):

    if not os.path.exists(KNOWLEDGE_PATH):

        return {
            "success": False,
            "error": "尚未建立專案知識"
        }


    with open(
        KNOWLEDGE_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)


    results = []


    text = json.dumps(
        data,
        ensure_ascii=False
    )


    if keyword.lower() in text.lower():

        results.append(
            data
        )


    return {
        "success": True,
        "keyword": keyword,
        "results": results
    }



def run():

    return {
        "success": True,
        "message": "Knowledge Tool ready"
    }

import json
import os


MEMORY_DIR = "memory"


def load_file(name):

    path = os.path.join(
        MEMORY_DIR,
        name
    )

    if not os.path.exists(path):
        return []


    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return []



def search_memory(query):

    results = []


    keywords = query.lower().split()



    # 長期記憶

    long_term = load_file(
        "long_term.json"
    )


    for item in long_term:

        content = item.get(
            "content",
            ""
        )


        if any(
            word in content.lower()
            for word in keywords
        ):

            results.append(
                {
                    "type": "long_term",
                    "content": content
                }
            )



    # 近期記憶

    recent = load_file(
        "recent.json"
    )


    for item in recent:

        content = item.get(
            "content",
            ""
        )


        if any(
            word in content.lower()
            for word in keywords
        ):

            results.append(
                {
                    "type": "recent",
                    "content": content
                }
            )



    # 去除重複

    unique = []

    seen = set()


    for item in results:

        content = item.get(
            "content",
            ""
        )


        if content not in seen:

            seen.add(content)

            unique.append(item)



    return unique

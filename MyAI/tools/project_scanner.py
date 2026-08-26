import os
import json


IGNORE = [
    "__pycache__",
    ".git",
    ".cache"
]


KNOWLEDGE_PATH = os.path.expanduser(
    "~/MyAI/knowledge/user/project.json"
)



def analyze(path="~"):

    path = os.path.expanduser(path)

    files = []


    for root, dirs, names in os.walk(path):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE
        ]


        for name in names:

            full = os.path.join(
                root,
                name
            )


            files.append(
                os.path.relpath(
                    full,
                    path
                )
            )



    result = {

        "project_path": path,

        "file_count": len(files),

        "files": files

    }


    save_knowledge(
        result
    )


    return result





def save_knowledge(data):

    folder = os.path.dirname(
        KNOWLEDGE_PATH
    )


    os.makedirs(
        folder,
        exist_ok=True
    )


    with open(
        KNOWLEDGE_PATH,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )




def run():

    return analyze()

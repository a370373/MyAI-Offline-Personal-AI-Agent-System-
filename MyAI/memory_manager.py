import os
import json


MEMORY_DIR = "memory"



FILES = {

    "history.json": [],

    "profile.json": {},

    "facts.json": [],

    "long_term.json": [],

    "user_memory.json": {}

}



def init_memory():

    if not os.path.exists(MEMORY_DIR):

        os.makedirs(
            MEMORY_DIR
        )


    for filename, default in FILES.items():

        path = os.path.join(
            MEMORY_DIR,
            filename
        )


        if not os.path.exists(path):

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    default,
                    f,
                    ensure_ascii=False,
                    indent=4
                )



def load_memory(filename):

    init_memory()


    path = os.path.join(
        MEMORY_DIR,
        filename
    )


    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return None



def save_memory(filename, data):

    init_memory()


    path = os.path.join(
        MEMORY_DIR,
        filename
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def clear_memory():

    for filename in FILES:

        path = os.path.join(
            MEMORY_DIR,
            filename
        )


        if os.path.exists(path):

            os.remove(path)


    init_memory()

import json
import os


FILE = "data/short_context.json"


def save_context(data):

    os.makedirs(
        "data",
        exist_ok=True
    )

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


def load_context():

    if not os.path.exists(FILE):
        return None


    try:

        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except:

        return None



def clear_context():

    if os.path.exists(FILE):

        os.remove(FILE)

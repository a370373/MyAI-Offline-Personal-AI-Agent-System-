import json
import os


BASE = "memory"


def load_memory(name):

    path = os.path.join(BASE, name)

    if not os.path.exists(path):
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)



def save_memory(name, data):

    path = os.path.join(BASE, name)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def get_profile():

    return load_memory("profile.json")



def get_facts():

    return load_memory("facts.json")



def add_fact(text):

    facts = get_facts()

    facts.append(text)

    save_memory(
        "facts.json",
        facts
    )

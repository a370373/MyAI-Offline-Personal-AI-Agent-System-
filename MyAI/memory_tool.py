from memory_manager import (
    load_memory,
    save_memory
)



def add_fact(content):

    facts = load_memory(
        "facts.json"
    )


    if not isinstance(facts, list):

        facts = []


    facts.append(
        {
            "content": content
        }
    )


    save_memory(
        "facts.json",
        facts
    )


    return {
        "success": True,
        "message": "已記憶"
    }



def get_facts():

    return load_memory(
        "facts.json"
    )



def clear_facts():

    save_memory(
        "facts.json",
        []
    )


    return {
        "success": True,
        "message": "已清除記憶"
    }

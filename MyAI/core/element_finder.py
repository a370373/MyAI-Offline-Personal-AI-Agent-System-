def find_input(elements, keyword):

    for e in elements:

        text = (
            str(e.get("placeholder"))
            +
            str(e.get("name"))
            +
            str(e.get("text"))
        )

        if keyword.lower() in text.lower():
            return e

    return None

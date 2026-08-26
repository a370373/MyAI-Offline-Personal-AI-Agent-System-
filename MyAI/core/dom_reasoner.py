class DOMReasoner:


    def analyze(self, elements):

        result = []


        for e in elements:

            role = None


            text = (
                str(e.get("aria") or "")
                +
                str(e.get("title") or "")
                +
                str(e.get("placeholder") or "")
            )


            text = text.lower()


            if (
                "搜尋" in text
                or
                "search" in text
            ):

                role = "searchbox"


            elif e.get("tag") in (
                "BUTTON",
                "INPUT"
            ):

                role = "button"



            result.append(
                {
                    "element": e,
                    "role": role
                }
            )


        return result


def simplify_dom(dom):

    if not dom:
        return []


    result=[]


    for e in dom:

        result.append(
            {
                "tag": e.get("tag",""),
                "text": (e.get("text") or ""),
                "aria": (e.get("aria") or ""),
                "title": (e.get("title") or ""),
                "placeholder": (e.get("placeholder") or ""),
                "id": (e.get("id") or ""),
                "name": (e.get("name") or ""),
                "x": e.get("x"),
                "y": e.get("y")
            }
        )


    return result

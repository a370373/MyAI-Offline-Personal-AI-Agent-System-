from core.dom_strategy import DOMStrategy

from core.experience_memory import ExperienceMemory


class ElementSelector:


    def __init__(self, finder):

        self.finder = finder

        self.memory = ExperienceMemory()



    def score(self, element, keyword):

        score = 0


        fields = [

            element.get("text",""),

            element.get("value",""),

            element.get("placeholder",""),

            element.get("aria",""),

            element.get("title",""),

            element.get("name",""),

            element.get("id","")

        ]


        text = " ".join(
            fields
        ).lower()


        keyword = keyword.lower()



        # 完全命中

        if keyword in text:

            score += 100



        # 分詞命中

        for word in keyword.split():

            if word in text:

                score += 20



        tag = element.get(
            "tag",
            ""
        )


        if tag in (
            "INPUT",
            "TEXTAREA"
        ):

            score += 40



        if tag in (
            "BUTTON",
            "A"
        ):

            score += 20



        if element.get("type") in (

            "submit",

            "button"

        ):

            score += 20



        if element.get("x") is not None:

            score += 5



        return score




    def candidates(self, keyword):

        results=[]


        methods=[

            "find_input",

            "find_text",

            "find_button",

            "find_link"

        ]



        for method in methods:

            try:

                fn=getattr(
                    self.finder,
                    method
                )

                r=fn(keyword)


                if r:

                    if isinstance(r,list):

                        results.extend(r)

                    else:

                        results.append(r)


            except Exception:

                pass




        unique=[]

        seen=set()

        for e in results:

            key=(

                e.get("tag"),

                e.get("id"),

                e.get("name"),

                e.get("x"),

                e.get("y")

            )

            if key not in seen:

                seen.add(key)

                unique.append(e)


        return unique




    def best(self, keyword):

        items=self.candidates(
            keyword
        )


        if not items:

            print(
                "[SELECT] no candidate"
            )

            return None



        ranked=sorted(

            items,

            key=lambda x:

            self.score(
                x,
                keyword
            ),

            reverse=True

        )



        print(

            "[SELECT]",

            self.score(
                ranked[0],
                keyword
            ),

            ranked[0]

        )


        return ranked[0]




    def debug(self, keyword):

        items=self.candidates(
            keyword
        )


        for e in items:

            print(

                "[CANDIDATE]",

                self.score(
                    e,
                    keyword
                ),

                e

            )


        return items
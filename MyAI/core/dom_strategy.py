class DOMStrategy:


    def infer(
        self,
        elements,
        intent
    ):


        candidates=[]


        for e in elements:


            text=" ".join([

                e.get("text",""),

                e.get("aria",""),

                e.get("placeholder",""),

                e.get("title","")

            ]).lower()



            score=0



            if intent in text:

                score+=50



            if intent=="search":

                if e.get("tag") in [
                    "INPUT",
                    "TEXTAREA"
                ]:

                    score+=50



                if e.get("role")=="searchbox":

                    score+=100



            candidates.append(
                (
                    score,
                    e
                )
            )



        candidates.sort(
            reverse=True,
            key=lambda x:x[0]
        )


        if candidates:

            print(
                "[DOM INFER]",
                candidates[0]
            )

            return candidates[0][1]


        return None

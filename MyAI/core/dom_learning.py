class DOMLearning:


    def rank(
        self,
        elements,
        target
    ):


        target=target.lower()


        for e in elements:


            text=" ".join([

                e.get("text",""),

                e.get("placeholder",""),

                e.get("aria",""),

                e.get("title","")

            ]).lower()



            score=0


            if target in text:

                score+=100



            if e.get("tag")=="INPUT":

                score+=30



            if e.get("role"):

                score+=20



            e["score"]=score



        return sorted(
            elements,
            key=lambda x:x.get(
                "score",
                0
            ),
            reverse=True
        )

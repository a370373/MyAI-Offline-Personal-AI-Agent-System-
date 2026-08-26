def score_element(element, target):


    score=0



    text=str(
        element
    ).lower()



    target=target.lower()



    if target in text:

        score += 50



    if "aria" in text:

        score += 20



    if "placeholder" in text:

        score += 20



    if "name" in text:

        score += 10



    if "input" in text:

        score += 10



    return score




def choose_best(elements,target):


    if not elements:

        return None



    ranked=[]


    for e in elements:

        ranked.append(

            (
                score_element(
                    e,
                    target
                ),

                e

            )

        )



    ranked.sort(

        reverse=True,

        key=lambda x:x[0]

    )


    return ranked[0][1]

import time
import random



def human_wait(
    min_time=0.5,
    max_time=1.5
):

    time.sleep(
        random.uniform(
            min_time,
            max_time
        )
    )




def human_type(
    page,
    text
):


    result = None


    for char in text:


        result = page.type_text(
            char
        )


        time.sleep(
            random.uniform(
                0.05,
                0.2
            )
        )



    return {

        "success": True,

        "action": "type",

        "text": text,

        "result": result

    }





def wait_page(
    page,
    timeout=10
):


    start = time.time()



    while time.time() - start < timeout:


        state = page.evaluate(
            "document.readyState"
        )


        try:

            value = (
                state["result"]
                ["result"]
                ["value"]
            )


            if value == "complete":

                return True


        except:

            pass



        time.sleep(
            0.5
        )



    return False

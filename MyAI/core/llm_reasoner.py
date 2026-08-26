import requests
import json
import time


LLAMA_URL = "http://127.0.0.1:8080/v1/chat/completions"



def ask_llm(prompt, retries=3):


    payload = {

        "messages":[

            {
                "role":"system",
                "content":
"""
你是 MyAI Browser Agent。

你負責控制瀏覽器完成任務。

只輸出 JSON。

允許 action:

open:
{
"action":"open",
"url":"網址"
}

find:
{
"action":"find",
"target":"元素名稱"
}

type:
{
"action":"type",
"target":"元素名稱",
"text":"輸入文字"
}

click_element:
{
"action":"click_element",
"target":"元素名稱"
}

read:
{
"action":"read"
}

完成或無法繼續:

{
"action":"stop",
"reason":"原因"
}


規則:
1. 不要重複已完成操作。
2. 不要一直 open 同一網址。
3. 優先根據 DOM 找元素。
4. 不要輸出解釋，只輸出 JSON。
"""
            },

            {
                "role":"user",
                "content":prompt
            }

        ],

        "temperature":0.2,

        "max_tokens":256

    }



    for i in range(retries):

        try:

            print(
                "[LLM] request",
                i+1
            )


            r=requests.post(

                LLAMA_URL,

                json=payload,

                timeout=180

            )


            data=r.json()


            return (
                data["choices"][0]
                ["message"]
                ["content"]
            )



        except Exception as e:


            print(
                "[LLM ERROR]",
                e
            )


            if i < retries-1:

                time.sleep(2)



    return None






def reason(
    goal,
    dom,
    state=None
):


    if state is None:

        state={}



    prompt=f"""

任務:

{goal}


目前 DOM:

{dom}


目前狀態:

{json.dumps(
    state,
    ensure_ascii=False
)}


請決定下一步瀏覽器操作。

注意:
如果任務已完成，輸出 stop。
不要重複之前 action。
只輸出 JSON。
"""



    output=ask_llm(
        prompt
    )



    if not output:


        return {

            "action":"stop",

            "reason":"LLM timeout"

        }




    try:


        output=output.strip()



        if "```" in output:


            output=(
                output
                .replace(
                    "```json",
                    ""
                )
                .replace(
                    "```",
                    ""
                )
                .strip()
            )



        return json.loads(
            output
        )



    except Exception:


        print(
            "[BAD JSON]",
            output
        )


        return {

            "action":"stop",

            "reason":
            "invalid json"

        }

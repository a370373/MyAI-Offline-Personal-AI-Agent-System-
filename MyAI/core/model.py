import requests

from config import LLAMA_SERVER, SYSTEM_PROMPT


def ask(user_input):

    data = {
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        "temperature": 0.7
    }


    response = requests.post(
        LLAMA_SERVER,
        json=data
    )


    result = response.json()


    if "choices" not in result:
        print("\n模型錯誤回傳：")
        print(result)
        return "模型服務異常"


    return result["choices"][0]["message"]["content"]

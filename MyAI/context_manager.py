import json
import os


CONTEXT_FILE = "memory/short_term/context.json"

MAX_MESSAGES = 6



def init_context():

    folder = os.path.dirname(
        CONTEXT_FILE
    )

    if not os.path.exists(folder):

        os.makedirs(folder)


    if not os.path.exists(CONTEXT_FILE):

        with open(
            CONTEXT_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {
                    "messages": [],
                    "pending_action": None
                },
                f,
                ensure_ascii=False,
                indent=4
            )



def load_context():

    init_context()

    try:

        with open(
            CONTEXT_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except:

        return {
            "messages": [],
            "pending_action": None
        }



def save_context(data):

    with open(
        CONTEXT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



# -------------------------
# Memory Filter
# -------------------------

def should_keep(role, content):


    if not content:

        return False



    # 不保存工具輸出

    if "<tool>" in content:

        return False



    # 不保存模型拒絕模板

    garbage = [
        "無法提供",
        "無法直接查詢",
        "建議您使用",
        "我無法"
    ]


    for word in garbage:

        if word in content:

            return False



    return True





def compress_content(content):


    # 避免巨大工具結果污染

    if len(content) > 1000:

        return content[:1000] + "\n[內容已截斷]"


    return content





def add_message(role, content):


    if not should_keep(
        role,
        content
    ):

        return



    content = compress_content(
        content
    )


    data = load_context()


    messages = data.get(
        "messages",
        []
    )


    # 去除完全重複

    if messages:

        last = messages[-1]


        if (
            last["role"] == role
            and
            last["content"] == content
        ):

            return



    messages.append(
        {
            "role": role,
            "content": content
        }
    )


    if len(messages) > MAX_MESSAGES:

        messages = messages[-MAX_MESSAGES:]



    data["messages"] = messages


    save_context(data)




def get_messages():

    return load_context().get(
        "messages",
        []
    )




def build_prompt_context():

    messages = get_messages()

    messages = messages[-6:]


    result = ""


    for msg in messages:

        result += (
            f"{msg['role']}:\n"
            f"{msg['content']}\n\n"
        )


    return result





def set_pending_action(action):

    data = load_context()

    data["pending_action"] = action

    save_context(data)




def get_pending_action():

    return load_context().get(
        "pending_action"
    )




def clear_pending_action():

    data = load_context()

    data["pending_action"] = None

    save_context(data)




def clear_context():

    save_context(
        {
            "messages": [],
            "pending_action": None
        }
    )

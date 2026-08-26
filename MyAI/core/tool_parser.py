import json

from core.tool_registry import list_tools



def get_tools():

    return [
        tool["name"]
        for tool in list_tools()
    ]



def parse_tool(text):


    TOOLS = get_tools()



    # ----------------
    # XML Tool Block
    # ----------------

    if "<tool>" in text and "</tool>" in text:


        data = text.split("<tool>")[1]

        data = data.split("</tool>")[0].strip()



        try:

            obj = json.loads(
                data
            )


            if obj.get("tool") in TOOLS:

                return obj


        except:

            pass



        # 舊格式相容

        if data in TOOLS:

            return {
                "tool": data
            }



    # ----------------
    # 直接 JSON
    # ----------------

    try:

        obj = json.loads(
            text
        )


        if obj.get("tool") in TOOLS:

            return obj


    except:

        pass



    # ----------------
    # 容錯搜尋
    # ----------------

    for tool in TOOLS:


        if tool in text:


            return {
                "tool": tool
            }



    return None

import os


def list_dir(path):

    path = os.path.expanduser(path)

    try:

        return "\n".join(
            os.listdir(path)
        )

    except Exception as e:

        return f"錯誤：{e}"



def tree(path, depth=2):

    path = os.path.expanduser(path)

    result = []


    def scan(current, level):

        if level > depth:
            return


        try:

            for item in os.listdir(current):

                full = os.path.join(
                    current,
                    item
                )

                prefix = "  " * level


                if os.path.isdir(full):

                    result.append(
                        f"{prefix}{item}/"
                    )

                    scan(
                        full,
                        level + 1
                    )

                else:

                    result.append(
                        f"{prefix}{item}"
                    )


        except Exception as e:

            result.append(
                f"錯誤：{e}"
            )


    scan(path, 0)

    return "\n".join(result)



def search(path, keyword):

    path = os.path.expanduser(path)

    result = []


    for root, dirs, files in os.walk(path):

        for file in files:

            if keyword.lower() in file.lower():

                result.append(
                    os.path.join(
                        root,
                        file
                    )
                )


    if result:

        return "\n".join(result)


    return "沒有找到相關檔案"



def read(path):

    path = os.path.expanduser(path)

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()


    except Exception as e:

        return f"錯誤：{e}"



def run():

    return tree("~/MyAI")

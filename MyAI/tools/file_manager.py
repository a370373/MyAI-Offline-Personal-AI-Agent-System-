import os

from tool_result import success, failure


IGNORE = [
    "__pycache__",
    ".git",
    ".cache"
]


IGNORE_EXT = [
    ".pyc",
    ".o",
    ".a"
]



def should_ignore(name):

    if name in IGNORE:
        return True


    for ext in IGNORE_EXT:

        if name.endswith(ext):
            return True


    return False



def tree(path, depth=3, mode="summary"):

    path = os.path.expanduser(path)

    result = []


    def scan(current, level):

        if level >= depth:
            return


        try:

            items = os.listdir(current)


            for item in sorted(items):

                if should_ignore(item):
                    continue


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


        except Exception:
            pass



    scan(path,0)



    return success(
        "file_manager",
        "tree",
        "\n".join(result)
    )



def list_dir(path):

    path = os.path.expanduser(path)

    try:

        files = []

        for item in os.listdir(path):

            if not should_ignore(item):

                files.append(item)


        return success(
            "file_manager",
            "list",
            "\n".join(files)
        )


    except Exception as e:

        return failure(
            "file_manager",
            "list",
            str(e)
        )



def read(path):

    path = os.path.expanduser(path)

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return success(
                "file_manager",
                "read",
                f.read()
            )


    except Exception as e:

        return failure(
            "file_manager",
            "read",
            str(e)
        )



def search(path, keyword):

    path = os.path.expanduser(path)

    result = []


    for root, dirs, files in os.walk(path):

        dirs[:] = [
            d for d in dirs
            if not should_ignore(d)
        ]


        for file in files:

            if should_ignore(file):
                continue


            if keyword.lower() in file.lower():

                result.append(
                    os.path.join(
                        root,
                        file
                    )
                )


    return success(
        "file_manager",
        "search",
        "\n".join(result)
        if result
        else "沒有找到"
    )



def run(path="~"):

    return tree(path)

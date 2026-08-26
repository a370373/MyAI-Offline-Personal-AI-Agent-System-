import os
from knowledge_manager import save_user



IGNORE = [
    "__pycache__",
    ".git",
    ".cache"
]



def scan_project(path):

    result = {
        "project_path": path,
        "files": {}
    }


    for root, dirs, files in os.walk(path):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE
        ]


        for file in files:

            full_path = os.path.join(
                root,
                file
            )


            relative = os.path.relpath(
                full_path,
                path
            )


            result["files"][relative] = {
                "type": get_type(file)
            }


    return result



def get_type(filename):

    if filename.endswith(".py"):

        return "Python source"


    if filename.endswith(".json"):

        return "Configuration/Data"


    if filename.endswith(".md"):

        return "Documentation"


    if filename.endswith(".sh"):

        return "Shell script"


    return "Unknown"



def analyze_project(path):

    knowledge = scan_project(
        path
    )


    save_user(
        knowledge
    )


    return {
        "success": True,
        "files": len(
            knowledge["files"]
        ),
        "saved": "knowledge/user/project.json"
    }

import re


HIGH_RISK = [
    "rm -rf",
    "rm -r",
    "mkfs",
    "dd",
    "format",
    "shutdown",
    "reboot",
    "chmod 777",
    "> /dev/"
]


MEDIUM_RISK = [
    "rm",
    "mv",
    "cp",
    "chmod",
    "kill",
    "pip uninstall",
    "apt remove"
]


def analyze(command):

    cmd = command.lower()

    for item in HIGH_RISK:
        if item in cmd:
            return {
                "level": "high",
                "message": f"危險操作：{item}"
            }


    for item in MEDIUM_RISK:
        if item in cmd:
            return {
                "level": "medium",
                "message": f"需要確認：{item}"
            }


    return {
        "level": "low",
        "message": "安全操作"
    }

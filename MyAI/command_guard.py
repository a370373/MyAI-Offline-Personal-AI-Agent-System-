DANGEROUS_COMMANDS = [
    "rm -rf",
    "rm -r",
    "mkfs",
    "dd if=",
    "format",
    "shutdown",
    "reboot"
]


def check(command):

    for danger in DANGEROUS_COMMANDS:

        if danger in command:
            return {
                "allow": False,
                "reason": "危險操作：" + danger
            }


    return {
        "allow": True,
        "reason": "允許執行"
    }

import subprocess
from tools.risk_analyzer import analyze


def run(command):

    risk = analyze(command)


    if risk["level"] == "high":
        return (
            "BLOCK\n"
            "危險操作："
            + risk["message"]
        )


    if risk["level"] == "medium":
        return (
            "CONFIRM\n"
            "需要確認\n"
            "指令："
            + command
        )


    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        output = result.stdout

        if not output:
            output = result.stderr

        return output or "執行完成"


    except Exception as e:
        return str(e)

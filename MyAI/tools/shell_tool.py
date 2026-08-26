import subprocess
from command_guard import check


def run(command):

    if not command:
        return "沒有收到指令"


    # 安全檢查
    result = check(command)


    if not result["allow"]:
        return "執行阻止：" + result["reason"]


    try:

        process = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=1000
        )


        output = process.stdout.strip()
        error = process.stderr.strip()


        if output:
            return output


        if error:
            return error


        return "指令執行完成（無輸出）"


    except subprocess.TimeoutExpired:

        return "仍在執行中，超過等待時間"


    except Exception as e:

        return "執行錯誤：" + str(e)

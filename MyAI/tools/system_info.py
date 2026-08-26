import os
import platform
import shutil
import subprocess


def run():

    info = {}

    info["OS"] = platform.system()
    info["架構"] = platform.machine()
    info["Python"] = platform.python_version()
    info["家目錄"] = os.path.expanduser("~")


    try:
        android = subprocess.check_output(
            ["getprop", "ro.build.version.release"],
            text=True
        ).strip()

        info["Android版本"] = android

    except:
        info["Android版本"] = "未知"


    try:
        total, used, free = shutil.disk_usage("/")

        info["儲存空間"] = {
            "總容量GB": round(total/1024**3,2),
            "已使用GB": round(used/1024**3,2),
            "剩餘GB": round(free/1024**3,2)
        }

    except:
        pass


    return info

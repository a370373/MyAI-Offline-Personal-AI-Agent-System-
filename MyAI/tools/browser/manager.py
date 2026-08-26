import subprocess
import time
import requests
import os


class BrowserManager:

    def __init__(self):
        self.port = 9222
        self.runtime = (
            "/data/data/com.termux/files/home/"
            "MyAI/runtime/browser/run-browser.sh"
        )
        self.process = None


    def is_running(self):

        try:
            r = requests.get(
                f"http://127.0.0.1:{self.port}/json/version",
                timeout=1
            )

            return r.status_code == 200

        except:
            return False


    def start(self):

        if self.is_running():
            return {
                "status": "already_running"
            }


        self.process = subprocess.Popen(
            [
                self.runtime
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


        for _ in range(20):

            if self.is_running():
                return {
                    "status": "started"
                }

            time.sleep(0.5)


        raise RuntimeError(
            "Browser failed to start"
        )


    def stop(self):

        os.system(
            "pkill headless-shell"
        )

        return {
            "status": "stopped"
        }

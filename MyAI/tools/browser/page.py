import requests
import websocket
import json
import itertools
import time


class PageController:

    def open(self,url):
        return self.navigate(url)



    def __init__(self):
        self.ws = None
        self.id = itertools.count(1)


    def create_page(self, url="about:blank"):

        r = requests.put(
            "http://127.0.0.1:9222/json/new?"
            + url
        )

        return r.json()


    def connect_page(self, ws_url):

        self.ws = websocket.create_connection(
            ws_url
        )


    def auto_connect(self):

        import requests
        import time


        tabs = requests.get(
            "http://127.0.0.1:9222/json"
        ).json()


        if not tabs:

            try:

                requests.put(
                    "http://127.0.0.1:9222/json/new?about:blank"
                )

                time.sleep(1)

                tabs = requests.get(
                    "http://127.0.0.1:9222/json"
                ).json()


            except Exception as e:

                print(
                    "[PAGE CREATE ERROR]",
                    e
                )

                return False



        if not tabs:
            return False



        ws_url = tabs[0].get(
            "webSocketDebuggerUrl"
        )


        if not ws_url:
            return False



        self.connect_page(
            ws_url
        )


        return True


    def send(self, method, params=None):

        if self.ws is None:

            ok = self.auto_connect()

            if not ok:
                raise RuntimeError(
                    "No active browser page"
                )

        if params is None:
            params = {}

        msg_id = next(self.id)

        self.ws.send(
            json.dumps({
                "id": msg_id,
                "method": method,
                "params": params
            })
        )

        while True:

            data = json.loads(
                self.ws.recv()
            )

            if data.get("id") == msg_id:
                return data


    def wait_ready(self, timeout=10):

        start = time.time()

        while time.time() - start < timeout:

            result = self.evaluate(
                "document.readyState"
            )

            try:

                state = result["result"]["result"]["value"]

                if state == "complete":
                    return True

            except:
                pass

            time.sleep(0.3)

        return False


    def navigate(self, url):

        result = self.send(
            "Page.navigate",
            {
                "url": url
            }
        )

        self.wait_ready()

        return result


    def evaluate(self, expression):

        return self.send(
            "Runtime.evaluate",
            {
                "expression": expression,
                "returnByValue": True
            }
        )



    def get_html(self):

        result = self.evaluate(
            "document.documentElement.outerHTML"
        )

        try:
            return result["result"]["result"]["value"]
        except:
            return ""

    def screenshot(self):

        return self.send(
            "Page.captureScreenshot",
            {
                "format": "png"
            }
        )


    def click(self, x, y):

        self.send(
            "Input.dispatchMouseEvent",
            {
                "type": "mousePressed",
                "x": x,
                "y": y,
                "button": "left",
                "clickCount": 1
            }
        )

        return self.send(
            "Input.dispatchMouseEvent",
            {
                "type": "mouseReleased",
                "x": x,
                "y": y,
                "button": "left",
                "clickCount": 1
            }
        )


    def type_text(self, text):

        return self.send(
            "Input.insertText",
            {
                "text": text
            }
        )


    def press_key(self, key):

        return self.send(
            "Input.dispatchKeyEvent",
            {
                "type": "keyDown",
                "key": key
            }
        )


    def release_key(self, key):

        return self.send(
            "Input.dispatchKeyEvent",
            {
                "type": "keyUp",
                "key": key
            }
        )


    def press_enter(self):

        return self.send(
            "Input.dispatchKeyEvent",
            {
                "type": "keyDown",
                "key": "Enter",
                "code": "Enter",
                "windowsVirtualKeyCode": 13,
                "nativeVirtualKeyCode": 13
            }
        )




    def scroll(self, y=800):

        return self.send(
            "Input.dispatchMouseEvent",
            {
                "type":"mouseWheel",
                "x":500,
                "y":500,
                "deltaX":0,
                "deltaY":y
            }
        )




    def back(self):

        return self.send(
            "Page.getNavigationHistory",
            {}
        )


    def refresh(self):

        return self.send(
            "Page.reload",
            {
                "ignoreCache": True
            }
        )

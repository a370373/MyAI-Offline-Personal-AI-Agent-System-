import requests
import websocket
import json
import itertools


class CDPClient:
    def __init__(self, host="127.0.0.1", port=9222):
        self.host = host
        self.port = port
        self.ws = None
        self.counter = itertools.count(1)


    def connect(self):

        version = requests.get(
            f"http://{self.host}:{self.port}/json/version"
        ).json()

        ws_url = version["webSocketDebuggerUrl"]

        self.ws = websocket.create_connection(ws_url)

        return True


    def send(self, method, params=None):

        if params is None:
            params = {}

        msg_id = next(self.counter)

        payload = {
            "id": msg_id,
            "method": method,
            "params": params
        }

        self.ws.send(json.dumps(payload))

        while True:
            response = json.loads(
                self.ws.recv()
            )

            if response.get("id") == msg_id:
                return response

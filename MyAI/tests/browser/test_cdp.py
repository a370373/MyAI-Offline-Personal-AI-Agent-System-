from tools.browser.cdp import CDPClient


browser = CDPClient()

print("connecting")

browser.connect()

print("connected")


result = browser.send(
    "Target.createTarget",
    {
        "url": "https://example.com"
    }
)

print(result)

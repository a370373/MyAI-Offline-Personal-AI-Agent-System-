from tools.browser.manager import BrowserManager
from tools.browser.page import PageController


manager = BrowserManager()

print(manager.start())


page = PageController()


target = page.create_page(
    "https://example.com"
)


page.connect_page(
    target["webSocketDebuggerUrl"]
)


print(
    page.evaluate(
        "document.title"
    )
)


print(
    page.evaluate(
        "document.body.innerText"
    )
)


shot = page.screenshot()


with open(
    "screen.png",
    "wb"
) as f:
    import base64
    f.write(
        base64.b64decode(
            shot["result"]["data"]
        )
    )


print("screenshot saved")

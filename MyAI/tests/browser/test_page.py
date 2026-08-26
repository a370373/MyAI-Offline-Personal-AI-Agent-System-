from tools.browser.manager import BrowserManager
from tools.browser.page import PageController


manager = BrowserManager()

print(
    manager.start()
)


page = PageController()


target = page.create_page(
    "https://example.com"
)


print(target)


page.connect_page(
    target["webSocketDebuggerUrl"]
)


print(
    page.navigate(
        "https://example.com"
    )
)


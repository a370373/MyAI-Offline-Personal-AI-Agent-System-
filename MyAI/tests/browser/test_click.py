from tools.browser.manager import BrowserManager
from tools.browser.page import PageController
from tools.browser.dom import DOMController

import time


BrowserManager().start()


page = PageController()

target = page.create_page(
    "https://example.com"
)


page.connect_page(
    target["webSocketDebuggerUrl"]
)


time.sleep(2)


dom = DOMController(page)


print(
    dom.click_text(
        "Learn more"
    )
)

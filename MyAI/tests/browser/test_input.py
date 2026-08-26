from tools.browser.manager import BrowserManager
from tools.browser.page import PageController
import time


BrowserManager().start()

page = PageController()

target = page.create_page(
    "https://www.google.com"
)

page.connect_page(
    target["webSocketDebuggerUrl"]
)

time.sleep(3)

page.evaluate("""
document.body.innerHTML += `
<input id="myinput"
style="position:fixed;top:100px;left:100px;width:300px;height:40px">
`
""")


time.sleep(1)

page.click(
    250,
    120
)

page.type_text(
    "MyAI Browser Agent"
)


print("done")

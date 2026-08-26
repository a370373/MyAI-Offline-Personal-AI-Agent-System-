from tools.browser.manager import BrowserManager


browser = BrowserManager()


print(
    browser.start()
)


print(
    browser.is_running()
)

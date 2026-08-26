from tools.browser import browser


result = browser.info()

print(result)


result = browser.open(
    "https://example.com"
)

print(result)

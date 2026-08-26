import re


KNOWN_SITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "github": "https://github.com",
    "twitter": "https://twitter.com",
}


def resolve_browser_intent(text):

    text = text.lower()


    # 搜尋優先處理
    if "搜尋" in text or "search" in text or "查詢" in text:
        query = text

        for name, url in KNOWN_SITES.items():
            if name in text:
                return {
                    "intent": "search",
                    "query": query.replace("搜尋","").replace(name,"").strip(),
                    "site": url
                }

        return {
            "intent": "search",
            "query": query.replace("搜尋","").replace("查詢","").strip()
        }


    # 打開網站
    if "打開" in text or "開啟" in text:

        for name, url in KNOWN_SITES.items():

            if name in text:
                return {
                    "action": "open",
                    "url": url
                }


        # 抓網址
        match = re.search(
            r"(https?://\S+|[\w.-]+\.(com|org|net|io))",
            text
        )

        if match:

            url = match.group(1)

            url = (
                url
                .replace("打開", "")
                .replace("開啟", "")
                .strip()
            )

            if not url.startswith("http"):
                url = "https://" + url

            return {
                "action": "open",
                "url": url
            }


    return None

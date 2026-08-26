import urllib.request
from html.parser import HTMLParser


class TextExtractor(HTMLParser):

    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        if data.strip():
            self.text.append(data.strip())


def browser_read(url):

    try:

        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        with urllib.request.urlopen(req, timeout=10) as response:

            html = response.read().decode(
                "utf-8",
                errors="ignore"
            )


        parser = TextExtractor()

        parser.feed(html)


        text = "\n".join(
            parser.text
        )


        return {
            "success": True,
            "url": url,
            "content": text[:5000]
        }


    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

class BrowserController:


    def __init__(self):
        self.current_url = None
        self.page = ""


    def open(self, url):

        self.current_url = url

        return {
            "success": True,
            "action": "open",
            "url": url
        }


    def read(self):

        return {
            "success": True,
            "action": "read",
            "url": self.current_url,
            "content": self.page
        }


    def click(self, target):

        return {
            "success": True,
            "action": "click",
            "target": target
        }


    def input(self, target, text):

        return {
            "success": True,
            "action": "input",
            "target": target,
            "text": text
        }



browser = BrowserController()

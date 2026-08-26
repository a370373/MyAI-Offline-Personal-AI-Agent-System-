from core.adapters.google import GoogleAdapter


class AdapterManager:


    def __init__(self):

        self.adapters = [
            GoogleAdapter()
        ]


    def get(self, url):

        for adapter in self.adapters:

            if adapter.match(url):

                return adapter

        return None

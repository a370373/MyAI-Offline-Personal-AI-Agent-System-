from core.adapter_manager import AdapterManager


class SiteRuntime:


    def __init__(self):

        self.manager=AdapterManager()

        self.current=None



    def detect(self,url):

        try:

            self.current=self.manager.get(
                url
            )

            if self.current:

                print(
                    "[SITE ADAPTER]",
                    self.current.__class__.__name__
                )

            else:

                print(
                    "[SITE ADAPTER] default"
                )


        except Exception as e:

            print(
                "[ADAPTER ERROR]",
                e
            )


        return self.current



    def get_rule(self,name):

        if self.current and hasattr(
            self.current,
            name
        ):

            return getattr(
                self.current,
                name
            )


        return None

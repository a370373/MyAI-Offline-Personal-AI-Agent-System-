from core.adapter_manager import AdapterManager


class SiteAdapterRuntime:


    def __init__(self):

        self.manager = AdapterManager()



    def get_adapter(self,url):

        try:
            adapter=self.manager.get(url)

            if adapter:

                print(
                    "[ADAPTER]",
                    adapter.__class__.__name__
                )

                return adapter


        except Exception as e:

            print(
                "[ADAPTER ERROR]",
                e
            )


        return None

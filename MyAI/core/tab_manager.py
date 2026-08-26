class TabManager:


    def __init__(self):

        self.tabs={}

        self.current=None



    def add(
        self,
        tab_id,
        url=""
    ):

        self.tabs[tab_id]={
            "url":url,
            "memory":{}
        }

        self.current=tab_id



    def switch(
        self,
        tab_id
    ):

        if tab_id in self.tabs:

            self.current=tab_id

            return True


        return False



    def close(
        self,
        tab_id
    ):

        if tab_id in self.tabs:

            del self.tabs[tab_id]

            return True


        return False



    def current_tab(self):

        return self.tabs.get(
            self.current
        )

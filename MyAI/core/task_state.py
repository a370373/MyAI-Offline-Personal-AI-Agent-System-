class TaskState:


    def __init__(self):

        self.data = {

            "completed": [],

            "failed": [],

            "actions": [],

            "current_url": "",

            "last_dom": ""

        }



    def add_action(
        self,
        action,
        result
    ):

        self.data["actions"].append(
            {
                "action": action,
                "result": result
            }
        )



    def complete(
        self,
        text
    ):

        if text not in self.data["completed"]:

            self.data["completed"].append(
                text
            )



    def fail(
        self,
        text
    ):

        self.data["failed"].append(
            text
        )



    def update_dom(
        self,
        dom
    ):

        self.data["last_dom"] = dom



    def update_url(
        self,
        url
    ):

        self.data["current_url"] = url



    def export(self):

        return self.data

class LoginStateManager:

    def __init__(self):
        self.state = {
            "logged_in": False,
            "user": None
        }


    def update(self, data):

        if "user" in data:
            self.state["user"] = data["user"]

        if data.get("logged_in"):
            self.state["logged_in"] = True


    def is_logged_in(self):

        return self.state["logged_in"]


    def get_state(self):

        return self.state

class DOMMemory:

    def __init__(self):
        self.rules = {}


    def remember(
        self,
        site,
        intent,
        element
    ):

        if site not in self.rules:
            self.rules[site]={}


        self.rules[site][intent]=element


        print(
            "[DOM MEMORY SAVE]",
            site,
            intent
        )


    def recall(
        self,
        site,
        intent
    ):

        return self.rules.get(
            site,
            {}
        ).get(
            intent
        )

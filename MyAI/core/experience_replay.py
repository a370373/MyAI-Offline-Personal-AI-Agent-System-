from core.memory.store import MemoryStore



class ExperienceReplay:


    def __init__(self):

        self.memory=MemoryStore()

        self.data=self.memory.load(
            "experiences"
        )



    def record(
        self,
        goal,
        action,
        result
    ):


        item={

            "action":action,

            "success":
            result.get(
                "success",
                False
            )

        }


        if goal not in self.data:

            self.data[goal]=[]


        self.data[goal].append(
            item
        )


        self.memory.save(
            "experiences",
            self.data
        )



    def recall(
        self,
        goal
    ):

        return self.data.get(
            goal,
            []
        )

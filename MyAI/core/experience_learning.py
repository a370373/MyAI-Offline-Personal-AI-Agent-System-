import json
from pathlib import Path


class ExperienceLearning:


    def __init__(self):

        self.path=Path(
            "data/experience_learning.json"
        )

        self.data={}

        self.load()



    def load(self):

        try:

            if self.path.exists():

                self.data=json.loads(
                    self.path.read_text()
                )

        except:

            self.data={}



    def save(self):

        self.path.parent.mkdir(
            exist_ok=True
        )

        self.path.write_text(
            json.dumps(
                self.data,
                ensure_ascii=False,
                indent=2
            )
        )



    def remember(
        self,
        site,
        action,
        element
    ):


        self.data.setdefault(
            site,
            {}
        )


        self.data[site][action]=element


        self.save()


        print(
            "[LEARN]",
            site,
            action
        )



    def recall(
        self,
        site,
        action
    ):


        return self.data.get(
            site,
            {}
        ).get(
            action
        )



    def show(self):

        return self.data

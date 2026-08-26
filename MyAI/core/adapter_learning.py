import json
from pathlib import Path


class AdapterLearning:


    def __init__(self):

        self.file=Path(
            "data/site_rules.json"
        )

        self.rules={}

        self.load()



    def load(self):

        if self.file.exists():

            try:

                self.rules=json.loads(
                    self.file.read_text()
                )

            except:

                self.rules={}



    def save(self):

        self.file.parent.mkdir(
            exist_ok=True
        )

        self.file.write_text(
            json.dumps(
                self.rules,
                ensure_ascii=False,
                indent=2
            )
        )



    def learn(
        self,
        site,
        rule
    ):


        self.rules.setdefault(
            site,
            {}
        )


        self.rules[site].update(
            rule
        )


        self.save()


        print(
            "[ADAPTER LEARN]",
            site,
            rule
        )



    def get(
        self,
        site
    ):

        return self.rules.get(
            site,
            {}
        )

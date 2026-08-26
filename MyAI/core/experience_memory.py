import json
from pathlib import Path


class ExperienceMemory:


    def __init__(self):

        self.file=Path(
            "data/experience.json"
        )

        self.file.parent.mkdir(
            exist_ok=True
        )

        if not self.file.exists():

            self.file.write_text(
                "[]"
            )



    def add(
        self,
        website,
        task,
        action,
        success=True
    ):


        data=json.loads(
            self.file.read_text()
        )


        data.append({

            "website":website,

            "task":task,

            "action":action,

            "success":success

        })


        self.file.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            )
        )



    def search(
        self,
        website,
        task
    ):


        data=json.loads(
            self.file.read_text()
        )


        return [

            x for x in data

            if x["website"]==website
            and x["task"]==task

        ]

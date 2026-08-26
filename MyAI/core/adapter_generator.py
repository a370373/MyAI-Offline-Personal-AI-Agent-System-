import json
from pathlib import Path


class AdapterGenerator:


    def __init__(self):

        self.file=Path(
            "data/site_rules.json"
        )

        self.file.parent.mkdir(
            exist_ok=True
        )


        if not self.file.exists():

            self.file.write_text(
                "{}"
            )



    def generate(
        self,
        url,
        target,
        element
    ):


        data=json.loads(
            self.file.read_text()
        )


        site=url.split("/")[2]


        if site not in data:

            data[site]={}



        data[site][target]={

            "tag":
            element.get("tag"),

            "id":
            element.get("id"),

            "name":
            element.get("name"),

            "placeholder":
            element.get("placeholder"),

            "confidence":0.8

        }


        self.file.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            )
        )


        return True

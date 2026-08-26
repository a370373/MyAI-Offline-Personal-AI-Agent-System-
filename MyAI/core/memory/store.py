import json
from pathlib import Path


class MemoryStore:


    def __init__(self):

        self.path = Path(
            "core/memory/data"
        )

        self.path.mkdir(
            parents=True,
            exist_ok=True
        )


    def save(
        self,
        name,
        data
    ):

        file=self.path / (
            name + ".json"
        )

        file.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            )
        )


    def load(
        self,
        name
    ):

        file=self.path / (
            name + ".json"
        )

        if not file.exists():

            return {}


        return json.loads(
            file.read_text()
        )

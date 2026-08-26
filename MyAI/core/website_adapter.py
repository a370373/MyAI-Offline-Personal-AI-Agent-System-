from core.adapter_generator import AdapterGenerator
from core.memory.store import MemoryStore


class WebsiteAdapter:


    def __init__(self):

        self.generator=AdapterGenerator()

        self.memory=MemoryStore()

        # 啟動自動載入
        self.rules=self.memory.load(
            "adapters"
        )

        print(
            "[ADAPTER LOAD]",
            self.rules.keys()
        )



    def learn(
        self,
        url,
        target,
        element
    ):


        rule=self.generator.generate(
            url,
            element
        )


        if url not in self.rules:

            self.rules[url]={}


        self.rules[url][target]=rule


        self.memory.save(
            "adapters",
            self.rules
        )


        print(
            "[ADAPTER SAVE]",
            url,
            target
        )


        return rule




    def match(
        self,
        url,
        target
    ):


        rule=self.rules.get(
            url,
            {}
        ).get(
            target
        )


        if rule:

            print(
                "[ADAPTER HIT]",
                rule
            )


        return rule

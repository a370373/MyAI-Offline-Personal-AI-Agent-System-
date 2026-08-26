class SkillRouter:


    def __init__(self,agent):

        self.agent=agent


        self.skills={

            "search":
            self.search_skill,

            "login":
            self.login_skill,

            "form":
            self.form_skill,

            "browser":
            self.browser_skill

        }



    def select(self,intent):

        name=intent.get(
            "intent",
            "browser"
        )


        if name in self.skills:

            print(
                "[SKILL]",
                name
            )

            return self.skills[name]


        return self.browser_skill




    def search_skill(self,intent):

        return [

            {
                "action":"open",
                "url":
                "https://www.google.com"
            },

            {
                "action":"wait",
                "seconds":2
            },

            {
                "action":"find",
                "target":"搜尋"
            },

            {
                "action":"type",
                "text":
                intent.get(
                    "query",
                    ""
                )
            },

            {
                "action":"press_enter"
            }

        ]




    def login_skill(self,intent):

        return [

            {
                "action":"find",
                "target":"登入"
            },

            {
                "action":"click"
            }

        ]




    def form_skill(self,intent):

        return [

            {
                "action":"find",
                "target":
                intent.get(
                    "target",
                    ""
                )
            }

        ]




    def browser_skill(self,intent):

        return [

            {
                "action":"wait",
                "seconds":1
            }

        ]

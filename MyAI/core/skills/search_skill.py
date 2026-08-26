class SearchSkill:


    def execute(self,query):

        return [

            {
                "action":"open",
                "url":"https://www.google.com"
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
                "text":query
            },

            {
                "action":"press_enter"
            }

        ]

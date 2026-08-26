class WebStrategy:


    common_inputs={

        "search":[
            "搜尋",
            "search",
            "query",
            "q"
        ],

        "login":[
            "登入",
            "login",
            "sign in"
        ],

        "password":[
            "密碼",
            "password",
            "passwd"
        ]

    }



    def detect(self,dom):

        result={}


        text=str(dom).lower()


        for key,values in self.common_inputs.items():

            for v in values:

                if v.lower() in text:

                    result[key]=v
                    break


        return result

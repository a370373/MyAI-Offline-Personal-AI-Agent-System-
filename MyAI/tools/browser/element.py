import json


class ElementFinder:

    def find_all(self):
        return self.get_elements()



    def __init__(self,page):
        self.page=page


    def _parse(self,result):
        try:
            value=result["result"]["result"]["value"]
            return json.loads(value)
        except:
            return []


    def get_elements(self):

        js="""
        (()=>{
            let result=[];

            let selectors=[
                "input",
                "textarea",
                "button",
                "a",
                "[role=button]",
                "[contenteditable=true]"
            ];

            for(let s of selectors){

                for(let e of document.querySelectorAll(s)){

                    let r=e.getBoundingClientRect();
                    let style=getComputedStyle(e);

                    if(
                        r.width>0 &&
                        r.height>0 &&
                        style.display!="none"
                    ){

                        result.push({

                            tag:e.tagName,

                            text:e.innerText || "",

                            value:e.value || "",

                            placeholder:e.placeholder || "",

                            aria:e.getAttribute(
                                "aria-label"
                            ) || "",

                            role:e.getAttribute(
                                "role"
                            ) || "",

                            title:e.title || "",

                            id:e.id || "",

                            name:e.name || "",

                            type:e.type || "",

                            x:r.left+r.width/2,

                            y:r.top+r.height/2

                        });

                    }
                }
            }


            return JSON.stringify(result);

        })()
        """


        return self._parse(
            self.page.evaluate(js)
        )





    def find_all(self, keyword):

        elements = self.get_elements()

        return [
            e for e in elements
            if self.score(e, keyword) > 0
        ]

    def score(self,e,keyword):

        score=0


        text=" ".join([

            e.get("text",""),

            e.get("value",""),

            e.get("placeholder",""),

            e.get("aria",""),

            e.get("title",""),

            e.get("id",""),

            e.get("name",""),

            e.get("role","")

        ]).lower()


        keyword=keyword.lower()


        if keyword in text:
            score+=100


        # Universal DOM Strategy

        aliases={

            "搜尋":[
                "search",
                "搜尋",
                "搜索"
            ],

            "search":[
                "search",
                "搜尋",
                "搜索"
            ],

            "輸入":[
                "input",
                "textarea",
                "textbox"
            ]

        }


        for key,words in aliases.items():

            if key in keyword:

                for word in words:

                    if word in text:

                        score+=40


        if (
            "search" in keyword
            or
            "搜尋" in keyword
        ):

            if e["tag"] in [
                "INPUT",
                "TEXTAREA"
            ]:
                score+=80


            if e.get("role")=="searchbox":
                score+=100



        if e["tag"] in [
            "INPUT",
            "TEXTAREA"
        ]:
            score+=30


        if e["tag"]=="BUTTON":
            score+=20
# input priority
        tag = e.get("tag","").lower()
        name = e.get("name","").lower()
        typ = e.get("type","").lower()
        role = e.get("role","").lower()

        if tag in ["textarea"]:
            score += 300

        if tag == "input":
            if typ in ["text","search"]:
                score += 300

            if name == "q":
                score += 500

        # submit button penalty
        if typ == "submit":
            score -= 300

        if role == "button":
            score -= 100

        return score



    def find_best(self,keyword):

        elements=self.get_elements()


        if not elements:
            return None


        ranked=sorted(
            elements,
            key=lambda x:self.score(x,keyword),
            reverse=True
        )


        best=ranked[0]


        print(
            "[DOM BEST]",
            best,
            "score=",
            self.score(
                best,
                keyword
            )
        )


        if self.score(best,keyword)<=0:
            return None


        return best



    def find_text(self,text):

        return self.find_best(text)



    def find_input(self,text=""):

        return self.find_best(text)

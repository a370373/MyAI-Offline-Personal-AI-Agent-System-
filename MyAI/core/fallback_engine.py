import json


class FallbackEngine:


    def __init__(self, page):

        self.page = page



    def parse(self, result):

        try:

            value = result["result"]["result"]["value"]

            if value:

                return json.loads(value)

        except:

            pass


        return None



    def search(self, keyword):


        js = f"""

        (() => {{

            let key = {json.dumps(keyword)};


            let elements = Array.from(
                document.querySelectorAll(
                    "*"
                )
            );


            let result=[];


            for(let e of elements){{


                let text = (

                    e.innerText ||

                    e.placeholder ||

                    e.getAttribute("aria-label") ||

                    e.id ||

                    e.name ||

                    ""

                ).toLowerCase();



                if(
                    text.includes(
                        key.toLowerCase()
                    )
                ){{


                    let r =
                    e.getBoundingClientRect();



                    if(
                        r.width > 0 &&
                        r.height > 0
                    ){{


                        result.push({{

                            tag:e.tagName,

                            text:
                            e.innerText || "",


                            id:e.id || "",


                            name:e.name || "",


                            placeholder:
                            e.placeholder || "",


                            x:
                            r.left+r.width/2,


                            y:
                            r.top+r.height/2


                        }});

                    }}

                }}

            }}


            return JSON.stringify(
                result.slice(0,20)
            );


        }})()

        """


        return self.parse(
            self.page.evaluate(js)
        )

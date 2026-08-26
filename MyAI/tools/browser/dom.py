import json


class DOMController:

    def __init__(self, page):
        self.page = page


    def get_elements(self):

        js = """
        (() => {

        let result=[];

        let elements=document.querySelectorAll(
            "a,button,input,textarea,select,[role]"
        );


        elements.forEach((e,index)=>{

            let r=e.getBoundingClientRect();

            if(
                r.width>0 &&
                r.height>0
            ){

            result.push({

                "id":index,

                "tag":e.tagName,

                "text":
                    e.innerText ||
                    e.value ||
                    e.placeholder ||
                    "",

                "type":
                    e.type || "",

                "name":
                    e.name || "",

                "placeholder":
                    e.placeholder || "",

                "x":
                    r.left+r.width/2,

                "y":
                    r.top+r.height/2

            });

            }

        });


        return JSON.stringify(result);

        })()
        """

        raw=self.page.evaluate(js)

        try:
            return json.loads(
                raw["result"]["result"]["value"]
            )

        except:
            return []


    def get_text(self):

        js="""

        document.body.innerText

        """

        result=self.page.evaluate(js)

        try:
            return result["result"]["result"]["value"]

        except:
            return ""

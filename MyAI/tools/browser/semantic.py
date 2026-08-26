import json


class SemanticMapper:

    def __init__(self, page):
        self.page = page


    def analyze(self):

        js = """
        (() => {

            let elements = [];

            let nodes = document.querySelectorAll(
                "input,button,a,textarea,select"
            );


            for(let e of nodes){

                let r = e.getBoundingClientRect();

                if(
                    r.width === 0 ||
                    r.height === 0
                )
                    continue;


                let text =
                    e.innerText ||
                    e.value ||
                    e.placeholder ||
                    e.ariaLabel ||
                    "";


                let type="unknown";


                if(
                    e.tagName==="INPUT" &&
                    (
                        e.type==="text" ||
                        e.type==="search"
                    )
                ){
                    type="search_or_text";
                }


                if(
                    e.tagName==="BUTTON" ||
                    e.tagName==="A"
                ){
                    type="clickable";
                }


                elements.push({

                    tag:e.tagName,
                    type:type,
                    text:text.trim(),

                    id:e.id || "",
                    name:e.name || "",
                    placeholder:e.placeholder || "",

                    x:r.left+r.width/2,
                    y:r.top+r.height/2

                });

            }


            return JSON.stringify(elements);

        })()
        """

        result = self.page.evaluate(js)

        try:

            return json.loads(
                result["result"]["result"]["value"]
            )

        except:

            return []

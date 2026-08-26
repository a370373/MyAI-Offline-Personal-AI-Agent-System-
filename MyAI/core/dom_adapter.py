class DOMAdapter:


    def normalize(self, elements):

        output=[]


        for e in elements:

            output.append({

                "tag":
                e.get("tag",""),

                "text":
                e.get("text",""),

                "aria":
                e.get("aria",""),

                "title":
                e.get("title",""),

                "id":
                e.get("id",""),

                "x":
                e.get("x"),

                "y":
                e.get("y")

            })


        return output


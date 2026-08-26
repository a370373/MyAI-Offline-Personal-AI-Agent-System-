class SPADetector:


    def detect(self,html):

        patterns=[
            "react",
            "vue",
            "angular",
            "__next",
            "webpack"
        ]

        html=html.lower()


        for p in patterns:

            if p in html:
                return True


        return False

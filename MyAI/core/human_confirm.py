class HumanConfirm:


    def request(self,reason):

        print(
            "\n[Human Confirm Required]"
        )

        print(reason)


        answer=input(
            "Continue? (y/n): "
        )


        return answer.lower()=="y"

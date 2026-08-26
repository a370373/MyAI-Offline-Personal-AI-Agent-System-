class ResultInterpreter:


    def explain(self, observation):

        if not observation:

            return "沒有取得結果。"


        if isinstance(observation, str):

            return observation



        if not observation.get("success", False):

            return (
                "任務執行失敗。\n"
                "原因："
                + str(observation.get("error","未知錯誤"))
            )



        dom = observation.get(
            "dom",
            ""
        )


        text = str(dom)



        # 簡單清理

        text = text.replace(
            "\\n",
            "\n"
        )


        if len(text) > 1000:

            text = text[:1000] + "\n..."



        return (
            "任務完成。\n\n"
            "觀察到的內容：\n"
            + text
        )

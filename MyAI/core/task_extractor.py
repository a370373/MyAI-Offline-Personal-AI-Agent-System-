import re


class TaskExtractor:


    def extract(self, text):

        tasks = []


        # =====================
        # Open URL
        # =====================

        url = re.search(
            r"([\w.-]+\.(?:com|org|net|io|tw))",
            text
        )

        if url:

            tasks.append({
                "intent": "open_url",
                "url": "https://" + url.group(1)
            })


        # =====================
        # Find element
        # =====================

        target = None


        find_match = re.search(
            r"找到\s*(.+?)(?=\s+(?:打(?!開)|輸入|填|送出|提交)|$)",
            text
        )


        if find_match:

            target = find_match.group(1).strip()


            # 保護常見 UI 名稱
            if "聊天輸入" in text:
                target = "聊天輸入"


            tasks.append({
                "intent": "find_element",
                "target": target
            })


            tasks.append({
                "intent": "click_element",
                "target": target
            })


        # =====================
        # Input text
        # =====================

        type_match = re.search(
            r"(?:^|\s)(?:打|輸入)\s*(?!開)(.+?)(?=\s+送出|\s+提交|$)",
            text
        )


        if type_match:

            value = type_match.group(1).strip()

            value = value.replace(
                "開 chatgpt.com",
                ""
            ).strip()


            # 清除殘留流程文字
            value = value.replace(
                "找到",
                ""
            )

            value = value.replace(
                "聊天輸入",
                ""
            )

            value = value.strip()


            tasks.append({
                "intent": "input_text",
                "target": target or "輸入框",
                "text": value
            })


        # =====================
        # Submit
        # =====================

        if (
            "送出" in text
            or "提交" in text
        ):

            tasks.append({
                "intent": "submit"
            })


        return tasks

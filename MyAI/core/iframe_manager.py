class IFrameManager:


    def find_frames(self,page):

        try:

            return page.frames

        except:

            return []


    def search_element(
        self,
        page,
        keyword
    ):

        for frame in self.find_frames(page):

            try:

                result = frame.query_selector(
                    keyword
                )

                if result:
                    return result

            except:
                continue


        return None

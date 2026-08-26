class MemoryRuntime:


    def __init__(self,memory=None):

        self.memory = memory


    def remember(self,data):

        if self.memory:

            return self.memory.save(
                data
            )

        return False


    def recall(self,key):

        if self.memory:

            return self.memory.get(
                key
            )

        return None


class LearningMemory:


    def __init__(self):

        self.failures=[]



    def add_failure(self, data):

        self.failures.append(data)



    def suggest(self):

        return self.failures[-5:]

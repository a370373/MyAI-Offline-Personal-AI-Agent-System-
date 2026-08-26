class ToolRuntime:


    def __init__(self,manager=None):

        self.manager=manager


    def execute(self,name,**kwargs):

        if not self.manager:

            return None


        tool=self.manager.get(name)


        if tool:

            return tool(**kwargs)


        return {
            "success":False,
            "error":"tool missing"
        }

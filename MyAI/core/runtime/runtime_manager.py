class RuntimeManager:


    def __init__(self, agent=None):

        self.agent = agent

        self.browser = None
        self.memory = None
        self.tools = None
        self.shell = None

        self.init_browser()


    def register(self, name, runtime):

        setattr(
            self,
            name,
            runtime
        )


    def get(self,name):

        return getattr(
            self,
            name,
            None
        )


    def status(self):

        return {

            "browser": self.browser is not None,

            "memory": self.memory is not None,

            "tools": self.tools is not None,

            "shell": self.shell is not None

        }


    def init_browser(self):

        try:
            from tools.browser.page import PageController
            from core.runtime.browser_runtime import BrowserRuntime
            from core.browser_agent import BrowserAgent

            page = PageController()
            page.auto_connect()

            agent = BrowserAgent(page)

            self.browser = BrowserRuntime(agent)

        except Exception as e:
            print("[Browser Init Error]", e)
            self.browser = None


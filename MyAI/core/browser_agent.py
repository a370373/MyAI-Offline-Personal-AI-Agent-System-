from core.dom_parser import parse_dom
from core.dom_reasoner import DOMReasoner
from core.adapter_manager import AdapterManager
from core.element_selector import ElementSelector
from tools.browser.element import ElementFinder

from core.login_state_manager import LoginStateManager
from core.cookie_manager import CookieManager
from core.captcha_detector import CaptchaDetector
from core.human_confirm import HumanConfirm

from core.browser_runtime import BrowserRuntime
from core.browser_state import BrowserState
from core.page_waiter import PageWaiter
from core.iframe_manager import IFrameManager
from core.smart_scroll import SmartScroll
from core.spa_detector import SPADetector
from core.browser_brain import BrowserBrain


class BrowserAgent:


    def __init__(self, browser):

        self.browser = browser

        self.adapter_manager = AdapterManager()

        self.reasoner = DOMReasoner()
        self.brain = BrowserBrain()

        self.finder = ElementFinder(browser)

        self.login = LoginStateManager()
        self.cookies = CookieManager(browser)
        self.captcha = CaptchaDetector()
        self.human = HumanConfirm()
        self.state = BrowserState()

        self.waiter = PageWaiter()
        self.frames = IFrameManager()
        self.scroll = SmartScroll()
        self.spa = SPADetector()

        self.runtime = BrowserRuntime(
            self
        )



    def understand(self):

        html = self.browser.get_html()

        dom = parse_dom(html)

        return dom





    def run_goal(self, goal):

        dom = self.understand()


        state = self.brain.analyze(
            dom,
            goal
        )


        action = state.get(
            "next_action"
        )


        if not action:

            return {
                "success": False,
                "error": "no action"
            }


        if action["action"] == "find_input":

            element = self.find_best(
                action.get("target","")
            )


            if element:

                return {
                    "success": True,
                    "next": {
                        "action":"type",
                        "element":element,
                        "text":goal
                    }
                }


        return {
            "success":False,
            "state":state
        }


    def get_adapter(self,url):

        return self.adapter_manager.get(
            url
        )



    def analyze(self):

        dom = self.understand()

        return self.reasoner.analyze(
            dom
        )



    def find_best(self,keyword):

        elements = self.finder.find_all(
            keyword
        )

        if not elements:
            return None


        return ElementSelector(
            self.finder
        ).best(
            keyword
        )





    def smart_type(self,text):

        element=self.find_best(
            "搜尋"
        )


        if element is None:

            return {
                "success":False,
                "error":"search box not found"
            }


        return {

            "success":True,

            "action":"type",

            "element":element,

            "text":text

        }


    def think(self,goal):

        dom=self.understand()

        return self.brain.analyze(
            dom,
            goal
        )


def type_text(self,element,text):

    x=element.get("x")
    y=element.get("y")


    js=f"""
    (()=>{{

    let e=document.elementFromPoint(
        {x},
        {y}
    );


    if(e){{
        e.focus();

        e.value="{text}";

        e.dispatchEvent(
            new Event(
                'input',
                {{
                bubbles:true
                }}
            )
        );

        return true;
    }}

    return false;

    }})()
    """


    return self.browser.page.evaluate(js)

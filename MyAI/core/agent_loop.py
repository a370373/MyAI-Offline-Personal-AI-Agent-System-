from core.action_resolver import ActionResolver
from core.browser_agent import BrowserAgent
from core.browser_recovery import BrowserRecovery
from core.llm_reasoner import reason
from core.dom_reasoner import simplify_dom

from core.action_validator import validate
from core.action_normalizer import normalize_action
from core.action_schema import validate_action
from core.failure_detector import detect_failure
from core.task_completion import check_complete
from core.task_state import TaskState
from core.recovery import Recovery
from core.task_planner import TaskPlanner
from core.intent_router import IntentRouter
from core.skill_router import SkillRouter

from core.dom_memory import DOMMemory
from core.website_adapter import WebsiteAdapter
from core.page_state import PageState
from core.recovery_controller import RecoveryController
from core.tab_manager import TabManager
from core.site_runtime import SiteRuntime
from core.goal_verifier import GoalVerifier

from core.element_selector import ElementSelector
from core.target_resolver import TargetResolver

from tools.browser.browser import run
from tools.browser.element import ElementFinder
from core.reflection import ReflectionEngine

from core.runtime import (
    RuntimeManager,
    BrowserRuntime,
    MemoryRuntime,
    ToolRuntime,
    ShellRuntime
)



MAX_STEPS = 10



class AgentLoop:


    def simplify_dom(self, dom):

        return simplify_dom(
            dom
        )



    def __init__(self):

        self.runtime = RuntimeManager(self)

        self.browser_agent = (
            self.runtime.browser.agent
            if self.runtime.browser
            else None
        )


        self.browser_recovery = BrowserRecovery(
            self.browser_agent.finder
        )
        self.reflection = ReflectionEngine()

        self.finder = ElementFinder(self)

        self.action_resolver = ActionResolver(
            self.finder
        )

        self.selector = ElementSelector(
            self.finder
        )

        self.target_resolver = TargetResolver(
            self.selector
        )

        from core.recovery_engine import RecoveryEngine
        from core.reflection import Reflection
        from core.experience_memory import ExperienceMemory

        self.recovery = RecoveryEngine(self)

        self.reflection = Reflection()

        self.experience = ExperienceMemory()


        self.intent_router = IntentRouter()

        self.skill_router = SkillRouter(
            self
        )

        self.task_planner = TaskPlanner()

        self.dom_memory = DOMMemory()

        self.recovery_controller = RecoveryController(
            self.browser_agent,
            self.dom_memory
        )

        self.website_adapter = WebsiteAdapter()

        self.page_state = PageState()
        self.tab_manager = TabManager()

        self.site_runtime = SiteRuntime()

        self.goal_verifier = GoalVerifier()



    def execute(self, action):


        act = action.get(
            "action"
        )


        print(
            "[EXECUTE]",
            act
        )


        if act == "stop":

            return {
                "success":False,
                "error":action.get(
                    "reason",
                    "stop"
                )
            }



        if act == "open":

            url=action.get(
                "url",
                ""
            )

            self.site_runtime.detect(
                url
            )

            result=self.runtime.browser.open(
                url
            )


            try:

                self.page_state.wait_ready(
                    self.browser_agent.page
                )

            except Exception as e:

                print(
                    "[READY ERROR]",
                    e
                )


            return result




        if act == "analyze_dom":

            dom = self.browser_agent.analyze()

            return {
                "success":True,
                "dom":dom
            }


        if act == "type" or act == "smart_type":

            text = action.get(
                "text",
                ""
            )

            result = self.runtime.browser.type(
                text
            )

            return result


        if act == "scroll":

            return self.runtime.browser.scroll(
                action.get(
                    "direction",
                    "down"
                )
            )


        if act == "back":

            return run(
                action="back"
            )



        if act == "refresh":

            return run(
                action="refresh"
            )



        if act == "screenshot":

            return run(
                action="screenshot"
            )



        if act == "read":

            return run(
                action="read"
            )



        if act == "find":


            target=action.get(
                "target",
                ""
            )


            element=None


            # Adapter memory

            try:

                rule=self.website_adapter.match(
                    self.browser_agent.current_url,
                    target
                )

                if rule:

                    print(
                        "[ADAPTER HIT]",
                        rule
                    )


            except Exception as e:

                print(
                    "[ADAPTER CHECK ERROR]",
                    e
                )



            # DOM fallback

            element=self.selector.best(
                target
            )



            if element:

                try:

                    self.website_adapter.learn(
                        self.browser_agent.current_url,
                        target,
                        element
                    )

                    print(
                        "[ADAPTER LEARNED]"
                    )


                except Exception as e:

                    print(
                        "[ADAPTER LEARN ERROR]",
                        e
                    )


            else:

                print(
                    "[DOM FAILED]",
                    target
                )



            return {

                "success":
                element is not None,

                "element":
                element

            }


        if act == "type":


            return run(

                action="type",

                text=action.get(
                    "text",
                    ""
                )

            )




        if act == "click":

            element=self.selector.best(
                action.get(
                    "target",
                    ""
                )
            )


            if element:

                return run(
                    action="click",
                    x=element.get("x"),
                    y=element.get("y")
                )


            return {
                "success":False,
                "error":"element not found"
            }





        if act == "press_enter":

            return self.runtime.browser.submit()


        if act == "submit":

            return run(
                action="press_enter"
            )

        if act == "click_element":


            element=self.selector.best(

                action.get(
                    "target",
                    ""

                )

            )


            if element:


                return run(

                    action="click",

                    x=element.get(
                        "x"
                    ),

                    y=element.get(
                        "y"
                    )

                )



            return {

                "success":False,

                "error":
                "element not found"

            }




        return {

            "success":False,

            "error":
            "unknown action"

        }






    def get_html(self):

        result=run(
            action="read"
        )

        return result.get(
            "content",
            ""
        )






    def run(
        self,
        goal,
        steps=MAX_STEPS
    ):


        intent=self.intent_router.route(
            goal
        )

        print(
            "[INTENT]",
            intent
        )


        plan=self.task_planner.plan(
            intent
        )

        print(
            "[PLAN]",
            plan
        )


        history=[]

        import copy

        plan=copy.deepcopy(plan)

        queue=copy.deepcopy(plan)

        print(
            "[IMMUTABLE PLAN]",
            queue
        )

        memory=TaskState()

        recovery=Recovery()

        retry_count=0



        for i in range(steps):


            print(
                "[STEP]",
                i+1
            )



            dom=self.browser_agent.understand()



            simple=simplify_dom(
                dom
            )



            memory.update_dom(
                simple
            )



            if queue:

                action=queue.pop(0)

                print(
                    "[QUEUE ACTION]"
                )


            else:

                action=reason(

                    goal,

                    simple,

                    memory.export()

                )

                print(
                    "[LLM ACTION]"
                )



            # LLM輸出整理

            # Queue action 保留 Planner 原始結果

            if not queue:

                action=normalize_action(
                    action
                )

                action=self.target_resolver.resolve(
                    action
                )

                action=validate_action(
                    action
                )

            else:

                print(
                    "[RAW QUEUE ACTION]",
                    action
                )


            # 防重複

            # Queue Planner action 保持原樣
            if not queue:

                action=validate(
                    action,
                    history
                )



            print(
                "[PLANNER MODE]"
            )


            print(
                "ACTION:",
                action
            )



            result=self.execute(
                action
            )


            # Recovery Controller

            try:

                self.recovery_controller.recover(
                    result
                )


            except Exception as e:

                print(
                    "[RECOVERY CONTROLLER ERROR]",
                    e
                )


            if self.goal_verifier.verify(
                goal,
                history,
                result,
                simple
            ):

                print(
                    "[GOAL VERIFIED]"
                )

                break


            if not self.reflection.check(
                goal,
                result
            ):

                if self.recovery.should_retry(
                    result
                ):

                    self.recovery.recover(result)



            print(
                "RESULT:",
                result
            )
            if recovery.should_retry(
                result,
                retry_count
            ):

                retry_count += 1

                print(
                    "[RECOVERY]",
                    retry_count
                )

                recovery.wait()

                continue

            retry_count = 0




            history.append(

                {
                    "action":action,

                    "result":result

                }

            )



            memory.add_action(
                action,
                result
            )


            # 任務完成判斷

            try:

                completed = check_complete(
                    goal,
                    history,
                    result,
                    simple
                )


                if completed:

                    print(
                        "[TASK COMPLETE]"
                    )

                    break


            except Exception as e:

                print(
                    "[COMPLETE CHECK ERROR]",
                    e
                )




            if isinstance(result,dict):


                if result.get(
                    "success"
                ) == False:


                    memory.fail(

                        str(
                            result.get(
                                "error"
                            )
                        )

                    )



            if action.get(
                "action"
            ) == "open":


                memory.complete(
                    "opened:" +
                    str(
                        action.get(
                            "url",
                            ""
                        )
                    )
                )



            if action.get(
                "action"
            ) == "type":


                memory.complete(
                    "typed"
                )



            if action.get(
                "action"
            ) == "click_element":


                memory.complete(
                    "clicked"
                )



            if action.get(
                "action"
            ) == "stop":


                print(
                    "[TASK STOP]"
                )

                break



        return history

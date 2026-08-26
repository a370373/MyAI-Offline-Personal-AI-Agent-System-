from core.result_formatter import format_result
from core.model import ask
from core.tool_parser import parse_tool
from core.action_controller import execute_actions
from core.planner import create_plan
from core.reflection import Reflection
from core.capability_checker import format_capabilities
from core.permission import check_permission
from core.memory_bridge import process_memory
from core.memory_retriever import search_memory
from core.reflection import check_result
from core.dom_observer import DOMObserver
from core.self_corrector import SelfCorrector
from core.observation import Observation
from core.result_interpreter import ResultInterpreter
from core.task_adapter import adapt
from core.browser_result_formatter import format_browser_result
from core.context_router import get_relevant_context
from core.short_context import (
    save_context,
    load_context,
    clear_context
)

from context_manager import (
    get_pending_action,
    set_pending_action,
    clear_pending_action,
    build_prompt_context
)

from core.knowledge_manager import get_knowledge
from core.task_router import route_task
from core.browser.intent import resolve_browser_intent
from core.action_planner import ActionPlanner
from core.task_extractor import TaskExtractor
from core.short_context_router import (
    get_follow_up_context
)

MAX_LOOPS = 3

runtime_manager = None



interpreter = ResultInterpreter()


observer = Observation(
    runtime_manager.browser
    if runtime_manager
    else None
)



task_extractor = TaskExtractor()
self_corrector = SelfCorrector(
    runtime_manager.browser
    if runtime_manager
    else None
)



CONFIRM_WORDS = [
    "可以",
    "好",
    "允許",
    "確認",
    "執行",
    "開始"
]




def build_context(user_input):

    context = ""

    try:
        knowledge = get_knowledge(
            user_input
        )
    except Exception:
        knowledge = ""

    try:
        memories = search_memory(
            user_input
        )
    except Exception:
        memories = ""


    context += f"""
目前可用能力：

{format_capabilities()}

規則：

- 只能使用存在工具
- 高風險操作需要確認
- 不要編造不存在功能

使用者訊息：

{user_input}

"""


    if knowledge:

        context += f"""

相關專案知識：

{knowledge}

"""


    if memories:

        context += f"""

相關記憶：

{memories}

"""


    return context




def handle(user_input, runtime=None):

    print("\n[DEBUG USER INPUT]")
    print(user_input)


    # memory
    process_memory(
        "user",
        user_input
    )


    # advanced short context
    try:
        follow_context = get_follow_up_context(
            user_input
        )

        if follow_context:
            return format_browser_result(
                follow_context["data"].get(
                    "result",
                    {}
                ),
                follow_context["data"].get(
                    "observation",
                    {}
                )
            )

    except Exception as e:
        print("[follow context error]", e)



    # pending confirm restore
    try:
        pending = get_pending_action()

        if (
            pending
            and user_input.strip()
            in CONFIRM_WORDS
        ):
            print("\n[PENDING CONFIRM]")

            result = execute_actions(
                [pending],
                browser=(
                    runtime.browser
                    if runtime
                    else None
                )
            )

            clear_pending_action()

            reflection = check_result(
                result
            )


            if not reflection.get(
                "success",
                False
            ):

                try:
                    result = self_corrector.correct(
                        result
                    )
                except Exception:
                    pass


            observation = {
                "execution_result": result,
                "reflection": reflection,
            }


            process_memory(
                "assistant",
                str(observation)
            )


            return interpreter.explain(
                {
                    "success": reflection.get(
                        "success",
                        False
                    ),

                    "error": reflection.get(
                        "error"
                    ),

                    "dom": observation.get(
                        "dom_after_action",
                        {}
                    )
                }
            )

    except Exception as e:
        print("[pending error]", e)



    # capability
    if any(
        x in user_input
        for x in [
            "列出目前工具",
            "有哪些工具",
            "目前能力",
            "可用工具"
        ]
    ):
        return format_capabilities()



    # browser
    browser_keywords = [
        "打開",
        "開啟",
        "網址",
        "網站",
        "點擊",
        "輸入",
        "搜尋",
        "按下",
        "送出"
    ]


    browser_task = any(
        x in user_input
        for x in browser_keywords
    )


    if browser_task:

        print("\n[BROWSER ROUTE]")


        tasks = task_extractor.extract(
            user_input
        )


        actions = adapt(
            tasks
        )

        # permission gate restore

        for tool in actions:

            permission = check_permission(
                tool
            )

            print("\n[權限檢查]")
            print(permission)

            if not permission.get(
                "allowed"
            ):

                set_pending_action(
                    tool
                )

                return (
                    "此操作需要使用者確認：\n"
                    +
                    permission.get(
                        "reason",
                        ""
                    )
                )



        result = execute_actions(
            actions,
            browser=(
                runtime.browser
                if runtime
                else None
            )
        )


        reflection = check_result(
            result
        )


        observation = {
            "execution_result": result,
            "reflection": reflection,
            "dom_after_action": {}
        }


        try:
            if runtime and runtime.browser:

                runtime.browser.wait_response()

                observation[
                    "dom_after_action"
                ] = runtime.browser.analyze()


        except Exception as e:

            observation[
                "error"
            ] = str(e)



        try:

            save_context(
                {
                    "last_task": "browser",
                    "result": result,
                    "observation": observation,
                    "reflection": reflection
                }
            )


        except Exception:
            pass



        if not reflection.get(
            "success",
            False
        ):

            try:

                result = self_corrector.correct(
                    result
                )

            except Exception:
                pass
        
        print("\n[DEBUG BEFORE INTERPRETER]")
        print("RESULT=", result)
        print("OBS=", observation)
        print("REFLECTION=", reflection)


        final = interpreter.explain(
            {
                "success": reflection.get(
                    "success",
                    False
                ),

                "error": reflection.get(
                    "error"
                ),

                "dom": observation.get(
                    "dom_after_action",
                    {}
                )
            }
        )


        process_memory(
            "assistant",
            final
        )


        return final



    # normal LLM

    context = build_context(
        user_input
    )


    response = ask(
        context
    )


    try:

        tool = parse_tool(
            response
        )


        if tool:

            print("\n[TOOL DETECTED]")
            print(tool)


            set_pending_action(
                tool
            )


            return (
                response
                +
                "\n\n等待執行確認。"
            )


    except Exception as e:

        print(
            "[tool bridge error]",
            e
        )


    return response


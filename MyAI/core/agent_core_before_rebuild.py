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
    "確認"
]



def build_context(user_input):

    context = ""


    knowledge = get_knowledge(
        user_input
    )


    memories = search_memory(
        user_input
    )

# Follow up browser context only
followup_browser = any(
    x in user_input
    for x in [
        "結果如何",
        "完成了嗎",
        "剛剛怎樣",
        "上一個操作",
        "繼續"
    ]
)



    context += f"""

目前可用能力：

{format_capabilities()}


規則：

- 只能使用存在的工具
- 工具執行前必須通過權限檢查
- 高風險操作需要確認
- 不要假設不存在的功能


使用者最新訊息：

{user_input}

"""


    if knowledge:

      context += f"""

相關專案知識：

{knowledge}

"""



    # Browser 任務隔離長期記憶

    if memories and not any(
        x in user_input
        for x in [
            "打開",
            "開啟",
            "點擊",
            "輸入",
            "瀏覽器",
            "網頁"
        ]
    ):

      context += f"""

相關記憶：

{memories}

"""




    return context





def handle(user_input, runtime=None):

    print('\n[DEBUG USER INPUT]')
    print(user_input)


    short_context = get_relevant_context(
        user_input
    )


    if short_context:

        print(
            "\n[ACTIVE SHORT CONTEXT]"
        )

        print(
            short_context
        )


    short_context = load_context()

    if short_context:

        print("\n[SHORT CONTEXT]")
        print(short_context)


    observation = None
    if any(x in user_input for x in [
        "列出目前工具",
        "有哪些工具",
        "目前能力",
        "可用工具"
    ]):
        return format_capabilities()


    process_memory(
        "user",
        user_input
    )
# Short Context Follow-up Router

    follow_context = get_follow_up_context(
        user_input
    )


    if follow_context:

        print(
            "\n[FOLLOW UP CONTEXT]"
        )

        print(
            follow_context
        )


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

    # Browser 任務優先，不允許普通 LLM 搶答

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
        k in user_input
        for k in browser_keywords
    )


    # ==========================
    # Browser Agent Entry
    # ==========================

    if browser_task:

        print("\n[BROWSER ROUTE]")

        tasks = task_extractor.extract(
            user_input
        )

        print("\n[Task Extract]")
        print(tasks)


        actions = adapt(tasks)

        print("\n[Actions]")
        print(actions)


        result = execute_actions(
            actions,
            browser=runtime.browser if runtime else None
        )

        print("\n[Browser Result]")
        print(result)


        reflection = check_result(
            result
        )


        dom_state = {}

        try:

            if runtime and runtime.browser:

                runtime.browser.wait_response()

                dom_state = runtime.browser.analyze()

        except Exception as e:

            dom_state = {
                "error": str(e)
            }


        observation = {

            "execution_result": result,

            "dom_after_action": dom_state,

            "reflection": reflection

        }


        print("\n[DOM AFTER ACTION]")
        print(observation)


        # Browser 短期上下文保存
        try:

            save_context(
                {
                    "last_task": "browser",
                    "result": result,
                    "observation": observation,
                    "reflection": reflection
                }
            )

            process_memory(
                "assistant",
                str({
                    "type": "browser_result",
                    "observation": observation,
                    "reflection": reflection
                })
            )

        except Exception as e:
            print("[context save error]", e)



        return format_browser_result(
            result,
            observation
        )





    # ------------------
    # 恢復待確認任務
    # ------------------

    # Short context router
follow_keywords=[
    "結果如何",
    "完成了嗎",
    "剛剛",
    "上一個",
    "狀態",
    "繼續"
]

use_short_context = any(
    x in user_input
    for x in follow_keywords
)

pending = get_pending_action()


    if pending and user_input.strip() in CONFIRM_WORDS:


        print(
            "\n[恢復待確認任務]"
        )

        print(pending)


        clear_pending_action()


        results = execute_actions(
            [pending]
        )


        if not results:
            result = {
                "success": False,
                "error": "empty action result"
            }

        else:
            result = results[0]



        print("\n[DEBUG RESULT]")
        print(result)


        print("\n[DEBUG RESULT]")
        print(result)

        reflection = check_result(
            result
        )





        # ===============================
        # Post Action DOM Observation
        # ===============================

        try:

            dom_state = {}

            if runtime and runtime.browser:

                runtime.browser.wait_response()

                dom_state = runtime.browser.analyze()


            observation = {

                "execution_result": result,





                "dom_after_action": dom_state

            }


            print("\n[POST ACTION DOM]")
            print(observation)


        except Exception as e:

            observation = {

                "execution_result": result,

                "dom_after_action": {},

                "error": str(e)

            }

        if reflection.get(
              "success",
              False
          ):


            print('\n[DEBUG BEFORE INTERPRETER]')
            print('RESULT=', result)
            print('OBSERVATION=', observation)
            print('REFLECTION=', reflection)
            final = interpreter.explain(
                  {
                      "tool_result": {
                          "important": [
                              r for r in result
                              if not (
                                  isinstance(r, dict)
                                  and "result" in r
                                  and isinstance(r["result"], dict)
                                  and (
                                      "frameId" in r["result"]
                                      or "loaderId" in r["result"]
                                      or "isDownload" in r["result"]
                                  )
                              )
                          ]
                      },
                      "observation": observation,
                      "reflection": reflection
                  }
              )



            process_memory(
                "assistant",
                final
            )


            try:

                human_answer = ask(
                    str({
                         "short_context": load_context(),
                         "tool_result": result,
                         "observation": observation,
                          "reflection": reflection
                    })
                    +
                    """

你是 MyAI 執行結果整理助手。

【短期上下文最高優先】

CURRENT_SHORT_CONTEXT 代表上一個立即完成的任務。

如果使用者詢問：
- 結果如何
- 剛剛怎樣
- 完成了嗎
- 狀態如何

必須優先回答 CURRENT_SHORT_CONTEXT。

禁止：
- 回答其他專案分析
- 列出檔案
- 使用無關歷史記憶
- 編造不存在結果

只能根據目前任務資料回答。


【短期上下文最高優先】

CURRENT_SHORT_CONTEXT 代表上一個立即完成的任務。

如果使用者詢問：
- 結果如何
- 剛剛怎樣
- 完成了嗎
- 狀態如何

必須優先回答 CURRENT_SHORT_CONTEXT。

禁止：
- 回答其他專案分析
- 列出檔案
- 使用無關歷史記憶
- 編造不存在結果

只能根據目前任務資料回答。


【最高規則】
你只能根據目前提供的 observation、tool_result、reflection 回答。

禁止：
- 使用歷史記憶推測目前結果
- 回答目前資料不存在的事情
- 把其他任務結果套用到目前任務
- 編造專案分析、下載、錯誤或成功狀態

目前任務類型可能包含：
- browser automation
- DOM 操作
- 工具執行

如果 observation 包含 DOM：
請描述實際 DOM 狀態。

如果 observation 顯示沒有完成：
請明確說明沒有完成。

如果沒有足夠資料：
請回答「沒有可確認的結果」。


只根據提供資料回答。

禁止：
- 編造不存在資訊
- 推測下載
- 推測錯誤


如果 DOM 有成功操作：
告訴使用者完成了什麼。


執行資料：

"""
                    +
                    str(observation)
                )

                return human_answer


            except Exception:

                return final



    # final fallback
    try:
        if "observation" in locals():

            # Browser 任務禁止 fallback 自由回答
            if "browser_task" in locals() and browser_task:

                return (
                    "瀏覽器任務已執行，"
                    "但沒有產生可整理結果。"
                )


            final_answer = ask(
                str({
                    "observation": observation,
                    "reflection": reflection if "reflection" in locals() else {}
                })
                +
                """

你是 MyAI 最終結果整理助手。

只根據資料回答。

請：
- 告訴使用者實際完成什麼
- 如果 DOM 有變化，描述 DOM 狀態
- 不要編造成功或失敗
- 不要說下載，除非資料包含下載

用自然人話回答。
"""
            )

            return final_answer

    except Exception:
        pass


    return "任務執行完成，但沒有可整理的結果。"

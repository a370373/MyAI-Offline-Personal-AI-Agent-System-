from core.intent_router import IntentRouter
from core.skill_router import SkillRouter


class Orchestrator:


    def __init__(self,agent):

        self.agent=agent

        self.router=IntentRouter()

        self.skills=SkillRouter(
            agent
        )


    def run(self,text):

        intent=self.router.route(
            text
        )


        print(
            "[INTENT]",
            intent
        )


        result=self.skills.execute(
            intent
        )


        print(
            "[RESULT]",
            result
        )


        return result

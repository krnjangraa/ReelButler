from fastapi import APIRouter

from pydantic import BaseModel


from agents.orchestrator_agent import (
    OrchestratorAgent
)
orchestrator = OrchestratorAgent()


router = APIRouter()





class ScriptRequest(BaseModel):

    topic: str



@router.post("/run-workflow")
def run_workflow(
    data: ScriptRequest
):

    result = orchestrator.run_workflow(
        data.topic
    )

    return {

        "response": result
    }
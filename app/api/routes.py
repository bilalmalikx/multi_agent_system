from fastapi import APIRouter
from app.services.agent_service import run_agent

router = APIRouter()

@router.post("/run-agent")
def run(data: dict):
    user_input = data.get("input")
    result = run_agent(user_input)
    
    return result
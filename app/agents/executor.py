from app.tools.custom_tools import simple_calculator
from app.graph.state import AgentState

def tool_agent(state: AgentState) -> AgentState:
    result = simple_calculator("2+2")  
    
    return {
        "tool_result": result,
        "messages": state["messages"] + ["Tool executed"]
    }
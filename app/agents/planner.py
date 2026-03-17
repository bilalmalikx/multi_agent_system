from app.core.tracing import get_llm
from app.graph.state import AgentState

def planner_agent(state: AgentState) -> AgentState:
    llm = get_llm()

    prompt = f"Create a plan for: {state['user_input']}"
    
    response = llm.invoke(prompt)
    
    return {
        "plan": response.content,
        "messages": state["messages"] + ["Planner done"]
    }
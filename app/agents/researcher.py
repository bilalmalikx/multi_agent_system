from app.core.tracing import get_llm
from app.graph.state import AgentState

def researcher_agent(state: AgentState) -> AgentState:
    llm = get_llm()
    prompt = f"Research based on plan: {state['plan']}"
    
    response = llm.invoke(prompt)
    
    return {
        "research": response.content,
        "messages": state["messages"] + ["Research done"]
    }
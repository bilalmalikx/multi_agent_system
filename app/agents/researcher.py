from app.core.tracing import get_llm

def researcher_agent(state):
    llm = get_llm()
    prompt = f"Research based on plan: {state['plan']}"
    
    response = llm.invoke(prompt)
    
    return {
        "research": response.content,
        "messages": state["messages"] + ["Research done"]
    }
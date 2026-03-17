from app.core.tracing import get_llm

def planner_agent(state):
    llm = get_llm()
    
    prompt = f"Create a plan for: {state['user_input']}"
    
    response = llm.invoke(prompt)
    
    return {
        "plan": response.content,
        "messages": state["messages"] + ["Planner done"]
    }
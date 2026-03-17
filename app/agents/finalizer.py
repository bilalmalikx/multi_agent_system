from app.core.tracing import get_llm

def final_agent(state):
    llm = get_llm()
    prompt = f"""
    Plan: {state['plan']}
    Research: {state['research']}
    Tool: {state['tool_result']}
    
    Give final answer.
    """
    
    response = llm.invoke(prompt)
    
    return {
        "final_output": response.content,
        "messages": state["messages"] + ["Finalized"]
    }
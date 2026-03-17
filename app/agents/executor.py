from app.tools.custom_tools import simple_calculator

def tool_agent(state):
    result = simple_calculator("2+2")  # dynamic later
    
    return {
        "tool_result": result,
        "messages": state["messages"] + ["Tool executed"]
    }
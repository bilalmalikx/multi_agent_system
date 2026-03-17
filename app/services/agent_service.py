from app.graph.workflow import build_graph

graph = build_graph()

def run_agent(user_input: str):
    state = {
        "user_input": user_input,
        "plan": "",
        "research": "",
        "tool_result": "",
        "final_output": "",
        "messages": []
    }

    result = graph.invoke(state)

    return result
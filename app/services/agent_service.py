from app.graph.workflow import build_graph
from app.graph.state import AgentState

graph = build_graph()

def run_agent(user_input: str) -> AgentState:
    state = get_initial_state(user_input)
    result = graph.invoke(state)
    return result
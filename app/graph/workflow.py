from langgraph.graph import StateGraph, END

from app.graph.state import AgentState
from app.agents.planner import planner_agent
from app.agents.researcher import researcher_agent
from app.agents.executor import tool_agent
from app.agents.finalizer import final_agent

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", researcher_agent)
    graph.add_node("tool", tool_agent)
    graph.add_node("final", final_agent)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "tool")
    graph.add_edge("tool", "final")
    graph.add_edge("final", END)

    return graph.compile()
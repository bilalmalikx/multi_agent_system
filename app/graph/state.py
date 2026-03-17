from typing import TypedDict, List

class AgentState(TypedDict):
    user_input: str
    plan: str
    research: str
    tool_result: str
    final_output: str
    messages: List[str]


def get_initial_state(user_input: str) -> AgentState:
    return {
        "user_input": user_input,
        "plan": "",
        "research": "",
        "tool_result": "",
        "final_output": "",
        "messages": []
    }
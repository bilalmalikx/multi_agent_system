from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    user_input: str
    plan: str
    research: str
    tool_result: str
    final_output: str
    messages: List[str]
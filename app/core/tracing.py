from langchain_openai import ChatOpenAI
from app.core.config import settings

def get_llm():
    llm = ChatOpenAI(
        model="gpt-4-0613",
        temperature=0.7,
        openai_api_key=settings.OPENAI_API_KEY,
        tracing_v2=settings.LANGSMITH_TRACING_V2,
        tracing_project=settings.LANGSMITH_PROJECT,
    )
    return llm
from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    LANGSMITH_API_KEY: str = os.getenv("LANGSMITH_API_KEY")
    LANGSMITH_TRACING_V2: bool = os.getenv("LANGSMITH_TRACING_V2", "false").lower() == "true"
    LANGSMITH_PROJECT: str = os.getenv("LANGSMITH_PROJECT", "multi-agent")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./agents.db")

settings = Settings()
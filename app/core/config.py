from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "SupportPulse AI Platform"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "sqlite:///./support_ai.db"
    
    # LLM Configuration: "mock" (default for free local execution) or "litellm"
    LLM_PROVIDER: str = "mock"
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    MODEL_NAME: str = "gpt-3.5-turbo"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()

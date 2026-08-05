"""
Application configuration using Pydantic Settings

"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Centralized Application settings
    """

    app_name: str = "agentic-qa-engineer"
    environment: str = "development" 
    debug: bool  = True

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8"
    )

# Shared application settings object
settings = Settings()
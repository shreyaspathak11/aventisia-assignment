from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, List

class Settings(BaseSettings):
    """
    Global Application Settings.
    The Single Source of Truth for all configurations.
    """
    
    # App Metadata
    APP_TITLE: str = "GitHub Cloud Connector"
    APP_DESCRIPTION: str = "A professional backend service to integrate with GitHub's API"
    APP_VERSION: str = "1.0.0"
    
    # API Routing & Documentation
    API_V1_STR: str = "/api/v1/github"
    GITHUB_TAGS: List[str] = ["GitHub APIs"]
    
    # GitHub Integration Constants
    GITHUB_BASE_URL: str = "https://api.github.com"
    GITHUB_ACCEPT_HEADER: str = "application/vnd.github.v3+json"
    
    # Authentication (Can be overridden in .env)
    GITHUB_CLIENT_ID: Optional[str] = None
    GITHUB_CLIENT_SECRET: Optional[str] = None

    # Load from .env file if it exists
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Global Settings Instance
settings = Settings()

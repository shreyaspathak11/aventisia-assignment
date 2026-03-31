from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, List

class Settings(BaseSettings):
    """
    Settings class that manages application-wide configuration parameters.
    Values can be overridden by environment variables or values in a .env file.
    """
    
    # Application Metadata for Swagger and Documentation
    APP_TITLE: str = "GitHub Cloud Connector"
    APP_DESCRIPTION: str = "A professional backend service to integrate with GitHub's API"
    APP_VERSION: str = "1.0.0"
    
    # API Routing and Prefixing
    API_V1_STR: str = "/api/v1/github"
    AUTH_PREFIX: str = "/api/v1/auth"
    GITHUB_TAGS: List[str] = ["GitHub"]
    AUTH_TAGS: List[str] = ["Auth"]
    
    # GitHub API Communication Constants
    GITHUB_BASE_URL: str = "https://api.github.com"
    GITHUB_ACCEPT_HEADER: str = "application/vnd.github.v3+json"
    
    # GitHub App Credentials (Expected to be provided in .env)
    GITHUB_CLIENT_ID: Optional[str] = None
    GITHUB_CLIENT_SECRET: Optional[str] = None
    
    # GitHub OAuth Integration Endpoint Parameters
    GITHUB_OAUTH_AUTHORIZE_URL: str = "https://github.com/login/oauth/authorize"
    GITHUB_OAUTH_TOKEN_URL: str = "https://github.com/login/oauth/access_token"
    GITHUB_REDIRECT_URI: str = "http://localhost:8000/api/v1/auth/callback"
    GITHUB_SCOPES: str = "repo user read:org gist"

    # Pydantic Settings configuration: defines the environment file to load
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Static singleton instance of application settings
settings = Settings()

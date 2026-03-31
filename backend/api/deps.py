from fastapi import Request
from services import GithubService, AuthService

def get_auth_service(request: Request) -> AuthService:
    """Provides an AuthService instance with the shared HTTP client."""
    return AuthService(client=request.app.state.http_client)

def get_github_service(request: Request) -> GithubService:
    """
    Retrieves the verified GitHub token from the request state (set by AuthMiddleware)
    and returns a GithubService instance pre-configured with the shared client.
    """
    # The middleware already verified and stored the token
    token = getattr(request.state, "github_token", None)
    
    return GithubService(
        token=token, 
        client=request.app.state.http_client
    )

import httpx
from config import settings

class AuthService:
    """
    AuthService encapsulates the core logic for the GitHub OAuth 2.0 handshake.
    It manages the redirection URL generation and the backend callback processing.
    """
    def __init__(self, client: httpx.AsyncClient):
        """
        Initializes the AuthService with the shared, app-wide HTTP client.
        """
        self.client = client

    def get_authorize_url(self) -> str:
        """
        Generates the GitHub authorization URL using the application's credentials.
        The user will be redirected here to authorize the GitHub Application.
        """
        return (
            f"{settings.GITHUB_OAUTH_AUTHORIZE_URL}?"
            f"client_id={settings.GITHUB_CLIENT_ID}&"
            f"redirect_uri={settings.GITHUB_REDIRECT_URI}&"
            f"scope={settings.GITHUB_SCOPES}"
        )

    async def exchange_code_for_token(self, code: str) -> str:
        """
        Exchanges a temporary authorization code for a permanent access token.
        Requests are made to GitHub's OAuth token endpoint via the shared HTTP client.
        """
        payload = {
            "client_id": settings.GITHUB_CLIENT_ID,
            "client_secret": settings.GITHUB_CLIENT_SECRET,
            "code": code,
            "redirect_uri": settings.GITHUB_REDIRECT_URI
        }
        headers = {"Accept": "application/json"}
        
        # Perform the backend token exchange
        resp = await self.client.post(
            settings.GITHUB_OAUTH_TOKEN_URL,
            json=payload,
            headers=headers
        )
        resp.raise_for_status()
        data = resp.json()
        
        # Handle specific GitHub defined error states
        if "error" in data:
            raise Exception(f"GitHub OAuth Error: {data.get('error_description', data['error'])}")
            
        return data["access_token"]

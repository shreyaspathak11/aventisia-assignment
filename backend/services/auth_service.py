import httpx
from config import settings

class AuthService:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    def get_authorize_url(self) -> str:
        """Generate the GitHub authorization URL."""
        return (
            f"{settings.GITHUB_OAUTH_AUTHORIZE_URL}?"
            f"client_id={settings.GITHUB_CLIENT_ID}&"
            f"redirect_uri={settings.GITHUB_REDIRECT_URI}&"
            f"scope={settings.GITHUB_SCOPES}"
        )

    async def exchange_code_for_token(self, code: str) -> str:
        """Exchange temporary code for a permanent access token."""
        payload = {
            "client_id": settings.GITHUB_CLIENT_ID,
            "client_secret": settings.GITHUB_CLIENT_SECRET,
            "code": code,
            "redirect_uri": settings.GITHUB_REDIRECT_URI
        }
        headers = {"Accept": "application/json"}
        
        resp = await self.client.post(
            settings.GITHUB_OAUTH_TOKEN_URL,
            json=payload,
            headers=headers
        )
        resp.raise_for_status()
        data = resp.json()
        
        if "error" in data:
            raise Exception(f"GitHub OAuth Error: {data.get('error_description', data['error'])}")
            
        return data["access_token"]

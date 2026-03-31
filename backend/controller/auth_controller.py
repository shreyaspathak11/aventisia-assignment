from fastapi.responses import RedirectResponse
from fastapi import Depends
from api.deps import get_auth_service
from services.auth_service import AuthService
from models import SuccessResponse
from utils.errors import handle_api_error

class AuthController:
    """
    AuthController coordinates the GitHub OAuth 2.0 flow.
    It manages initial user redirection and handles the secure callback process.
    """
    def __init__(self, service: AuthService = Depends(get_auth_service)):
        """
        Initializes the controller with an injected AuthService.
        """
        self.service = service

    async def login(self) -> RedirectResponse:
        """
        Generates the GitHub authorization URL and executes a 302 redirect.
        This sends the user to GitHub to grant permissions.
        """
        url = self.service.get_authorize_url()
        return RedirectResponse(url)

    async def callback(self, code: str) -> SuccessResponse:
        """
        Coordinates the exchange of an authorization code for a permanent token.
        Errors are caught and transformed via the handle_api_error utility.
        """
        try:
            token = await self.service.exchange_code_for_token(code)
            return SuccessResponse(
                message="GitHub authentication successful",
                data={"access_token": token}
            )
        except Exception as e:
            handle_api_error(e, "GitHub authentication failed")

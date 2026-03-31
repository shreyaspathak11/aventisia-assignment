from fastapi import HTTPException, Depends
from fastapi.responses import RedirectResponse
from api.deps import get_auth_service
from services.auth_service import AuthService
from models import SuccessResponse

class AuthController:
    def __init__(self, service: AuthService = Depends(get_auth_service)):
        self.service = service

    async def login(self) -> RedirectResponse:
        """Redirect the user to GitHub's authorization page."""
        url = self.service.get_authorize_url()
        return RedirectResponse(url)

    async def callback(self, code: str) -> SuccessResponse:
        """Handle the GitHub callback and return the access token as JSON."""
        try:
            token = await self.service.exchange_code_for_token(code)
            return SuccessResponse(
                message="GitHub authentication successful",
                data={"access_token": token}
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

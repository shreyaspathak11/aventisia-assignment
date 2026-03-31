from fastapi import APIRouter, Depends, Query
from controller.auth_controller import AuthController
from models import SuccessResponse

router = APIRouter()

@router.get("/login")
async def login(controller: AuthController = Depends()):
    """
    Initiates the GitHub OAuth 2.0 login sequence.
    This endpoint generates and redirects the client to the GitHub authorization URL.
    """
    return await controller.login()

@router.get("/callback", response_model=SuccessResponse)
async def callback(
    code: str = Query(..., description="The temporary code provided by GitHub"),
    controller: AuthController = Depends()
):
    """
    The secure callback hook for GitHub's authorization service.
    Exchanges the temporary code for a permanent access token and returns it to the client.
    """
    return await controller.callback(code)

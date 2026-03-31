from fastapi import APIRouter, Depends, Query
from controller.auth_controller import AuthController
from models import SuccessResponse

router = APIRouter()

@router.get("/login")
async def login(controller: AuthController = Depends()):
    """
    Start GitHub OAuth Login
    
    Visit this URL in your browser to begin the authorization process.
    """
    return await controller.login()

@router.get("/callback", response_model=SuccessResponse)
async def callback(
    code: str = Query(..., description="The temporary code provided by GitHub"),
    controller: AuthController = Depends()
):
    """
    GitHub Callback (Token Exchange)
    
    This endpoint is called automatically by GitHub after you authorize the app.
    It returns your permanent access token as a JSON response.
    """
    return await controller.callback(code)

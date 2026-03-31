from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from utils.context import user_context
from models import ErrorResponse
from config import settings

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. Skip auth for static/docs and OAuth paths
        if request.url.path in {"/docs", "/redoc", "/openapi.json", "/"} or "/auth/" in request.url.path:
            return await call_next(request)
        
        # 2. Extract Token
        auth = request.headers.get("Authorization", "")
        if not (auth.startswith("token ") or auth.startswith("Bearer ")):
            return self._error("Valid GitHub token is required in Authorization header", 401)
        
        token = auth.split(" ")[1]

        # 3. Verify & Identify using the shared client
        try:
            client = request.app.state.http_client
            # Verify and identity check (Heartbeat) using central settings
            resp = await client.get(
                f"{settings.GITHUB_BASE_URL}/user", 
                headers={
                    "Authorization": f"token {token}", 
                    "Accept": settings.GITHUB_ACCEPT_HEADER
                }
            )
            
            if resp.status_code != 200:
                return self._error("Invalid or expired GitHub token", 401)
            
            # Identify the user and set context
            user_data = resp.json()
            user_context.set(user_data)
            
            # Store for downstream use if needed
            request.state.github_token = token
            request.state.github_user = user_data
            
        except Exception:
            return self._error("Authentication service (GitHub) is currently unavailable", 500)

        return await call_next(request)

    def _error(self, message: str, code: int):
        """Uses the professional ErrorResponse model for and consistent API responses."""
        error_content = ErrorResponse(status=code, message=message)
        return JSONResponse(status_code=code, content=error_content.model_dump())

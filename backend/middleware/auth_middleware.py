from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from utils.context import user_context
from models import ErrorResponse
from config import settings

class AuthMiddleware(BaseHTTPMiddleware):
    """
    AuthMiddleware is a security interceptor that validates GitHub authorization 
    for incoming requests.
    """
    async def dispatch(self, request: Request, call_next):
        """
        Intercepts the request to verify the 'Authorization' header.
        Populates the user_context if a valid GitHub token is provided.
        Skips authentication for documentation and core OAuth handshake routes.
        """
        # 1. Bypass authentication for documentation paths and the OAuth login flow
        if request.url.path in {"/docs", "/redoc", "/openapi.json", "/"} or "/auth/" in request.url.path:
            return await call_next(request)
        
        # 2. Extract Authorization token
        auth = request.headers.get("Authorization", "")
        if not (auth.startswith("token ") or auth.startswith("Bearer ")):
            return self._error("Valid GitHub token is required in Authorization header", 401)
        
        token = auth.split(" ")[1]

        # 3. Perform a 'Identity Heartbeat' check against the GitHub API
        try:
            # Utilize the shared, app-wide asynchronous HTTP client
            client = request.app.state.http_client
            
            # Verify identity using the GitHub user endpoint
            resp = await client.get(
                f"{settings.GITHUB_BASE_URL}/user", 
                headers={
                    "Authorization": f"token {token}", 
                    "Accept": settings.GITHUB_ACCEPT_HEADER
                }
            )
            
            if resp.status_code != 200:
                return self._error("Invalid or expired GitHub token", 401)
            
            # Extract user metadata and populate the stateless global context
            user_data = resp.json()
            user_context.set(user_data)
            
            # Persist data in request state for downstream controller/service access
            request.state.github_token = token
            request.state.github_user = user_data
            
        except Exception:
            # Handle upstream service (GitHub) outages
            return self._error("Authentication service (GitHub) is currently unavailable", 500)

        return await call_next(request)

    def _error(self, message: str, code: int):
        """
        Formats and returns a standardized ErrorResponse for unauthorized or system errors.
        """
        error_content = ErrorResponse(status=code, message=message)
        return JSONResponse(status_code=code, content=error_content.model_dump())

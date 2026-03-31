import uvicorn
import httpx
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBearer

from api.v1.github_api import router as github_router
from api.v1.auth_api import router as auth_router
from middleware.auth_middleware import AuthMiddleware
from config import settings

# HTTPBearer setup for Swagger UI integration
# auto_error=False ensures our custom AuthMiddleware handles all identity verification
security = HTTPBearer(auto_error=False)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the application's lifespan events.
    Initializes a shared HTTP client across all threads during startup.
    Ensures safe resource cleanup on shutdown.
    """
    # Setup shared, high-performance async HTTP client
    app.state.http_client = httpx.AsyncClient()
    yield
    # Safely close client session on application stop
    await app.state.http_client.aclose()

# Main FastAPI application instance setup
app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    # Apply global security dependencies
    dependencies=[Depends(security)]
)

# Register custom authentication and context-management middleware
app.add_middleware(AuthMiddleware)

@app.get("/", include_in_schema=False)
async def root():
    """
    Internal root endpoint redirects to automatically generated Swagger documentation.
    """
    return RedirectResponse(url="/docs")

# Register Authentication routes
app.include_router(
    auth_router, 
    prefix=settings.AUTH_PREFIX, 
    tags=settings.AUTH_TAGS
)

# Register GitHub functional routes
app.include_router(
    github_router, 
    prefix=settings.API_V1_STR, 
    tags=settings.GITHUB_TAGS
)

# Local development entry point
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

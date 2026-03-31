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

# This defines the "Authorize" button in Swagger UI
# We set auto_error=False because our AuthMiddleware handles the actual verification
security = HTTPBearer(auto_error=False)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup shared HTTP client
    app.state.http_client = httpx.AsyncClient()
    yield
    # Safely close client
    await app.state.http_client.aclose()

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    # This applies the padlock icon to all endpoints in Swagger
    dependencies=[Depends(security)]
)

# Add Auth Middleware
app.add_middleware(AuthMiddleware)

# Root redirect
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

# Include functional routes using central config
app.include_router(
    auth_router, 
    prefix=settings.AUTH_PREFIX, 
    tags=settings.AUTH_TAGS
)

app.include_router(
    github_router, 
    prefix=settings.API_V1_STR, 
    tags=settings.GITHUB_TAGS
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

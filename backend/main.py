import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api.v1.auth_api import router as v1_router
from api.v2.auth_api import router as v2_router

app = FastAPI(
    title="GitHub Cloud Connector",
    description="""
    A modular GitHub connector that integrates with external GitHub APIs.
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Root redirect to documentation
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

# Include Routers


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

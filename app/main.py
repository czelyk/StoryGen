from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Generate creative stories using AI based on your prompt and genre."
)

app.include_router(api_router, prefix="/api/v1")

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router
from core.config import settings

"""
FastAPI entry point file.
"""
app = FastAPI(
    title=settings.project_name,
    openapi_url=f"{settings.api_v1_str}/openapi.json"
)

if settings.backend_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=[str(origin) for origin in settings.backend_cors_origins],
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.api_v1_str)

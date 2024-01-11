import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
from api.api_v1.api import api_router
from core.config import settings

"""
FastAPI entry point file. It can be run in two ways.
- `uvicorn app:app --reload`
- `python ./app.py`
"""  

def custom_generate_unique_id(route: APIRoute):
    """
    Customize the function used to generate unique IDs for the *path
    operations* shown in the generated OpenAPI. This is particularly
    useful when automatically generating clients.
    """  
    return f"{route.tags[0]}-{route.name}"

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import APIRouter

from api.api_v1.endpoints import orgs

api_router = APIRouter()
api_router.include_router(org.router, tags=['root'])
api_router.include_router(org.router, prefix='/orgs', tags=['orgs'])

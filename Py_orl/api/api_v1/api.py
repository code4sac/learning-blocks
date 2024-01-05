from fastapi import APIRouter

from api.api_v1.endpoints import orgs
from api.api_v1.endpoints import other
#from api.api_v1.endpoints import Academicsessions

api_router = APIRouter()
# api_router.include_router(orgs.router, tags=['root'])
api_router.include_router(orgs.router, prefix='/orgs', tags=['orgs'])
api_router.include_router(other.router, prefix='/other', tags=['other'])
#api_router.include_router(other.router, prefix='/Academicsessions', tags=['Academicsessions'])


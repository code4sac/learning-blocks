from fastapi import APIRouter

from api.api_v1.endpoints import orgs
from api.api_v1.endpoints import other
from api.api_v1.endpoints import oneroster
#from api.api_v1.endpoints import students_status

api_router = APIRouter()
# api_router.include_router(orgs.router, tags=['root'])
api_router.include_router(orgs.router, prefix='/orgs', tags=['orgs'])
api_router.include_router(other.router, prefix='/other', tags=['other'])
api_router.include_router(oneroster.AcademicSessions().router, prefix='/academicsessions', tags=['academicsessions'])
api_router.include_router(oneroster.Classes().router, prefix='/classes', tags=['classes'])
api_router.include_router(oneroster.Courses().router, prefix='/courses', tags=['courses'])
api_router.include_router(oneroster.Demographics().router, prefix="/demographics", tags=["demographics"])
api_router.include_router(oneroster.Enrollments().router, prefix="/enrollments", tags=["enrollments"])
api_router.include_router(oneroster.GradingPeriods().router, prefix="/gradingPeriods", tags=["gradingPeriods"])
api_router.include_router(oneroster.Orgs().router, prefix="/organizations", tags=["orgs"])
api_router.include_router(oneroster.Schools().router, prefix="/schools", tags=["schools"])
api_router.include_router(oneroster.Students().router, prefix="/students", tags=["students"])
api_router.include_router(oneroster.Teachers().router, prefix="/teachers", tags=["teachers"])
api_router.include_router(oneroster.Terms().router, prefix="/terms", tags=["terms"])
api_router.include_router(oneroster.Users().router, prefix="/users", tags=["users"])
#api_router.include_router(students_status.router, prefix='/students_status', tags=['students_status'])
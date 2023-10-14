from fastapi import APIRouter
import requests
from students_status import students_status

router = APIRouter(
    prefix="/students",
    tags=["Student"],
    responses={404: {"description": "Not found"}},
)

# @router.get("/")
# async def greeting():
#     return {"message":"Working"}

@router.get("/{school_code}/{api_token}")
async def read_students(school_code:str, api_token:str):
    url = f'https://demo.aeries.net/aeries/api/v5/schools/{school_code}/ReportCard/?cert={api_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"Message": "Not Found"}

@router.get("/{school_code}")
async def get_students(school_code:str):
    student_response = students_status()
    displayValues = student_response.get_students_by_status()
    return displayValues
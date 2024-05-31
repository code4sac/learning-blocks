from fastapi import APIRouter, Depends, HTTPException
import requests
from starlette.responses import JSONResponse, StreamingResponse

from api.api_v1.endpoints.current_grades import current_grades

router = APIRouter()


@router.get('/')
async def root():
    return {'message': 'Hello World'}


# @app.get('/teams', response_model=list[TeamOut])
# async def getTeams():
#     return teams
#
#
# @app.post('/team/{name}', response_model=TeamOut)
# async def scoreTeam(name: str, win: bool = True):
#     for team in teams:
#         if team.name == name:
#             if win:
#                 team.wins += 1
#             else:
#                 team.losses += 1
#             return team


# create the url name for the page
@router.get('/student-data')
# create a method that will return value you want to the browser to see
def read_student_info():
    url = 'https://demo.aeries.net/aeries/api/v5/enrollment/99400001/year/2020?cert=477abe9e7d27439681d62f4e0de1f5e1'

    response = requests.get(url)

    if response.status_code == 200:
        # print(response.json())
        return response.json()

    else:
        return {}


# create the url name for the page
@router.get('/download-data')
# create a method that will return value you want to the browser to see
def download_student_info():
    url = 'https://demo.aeries.net/aeries/api/v5/enrollment/99400001/year/2020?cert=477abe9e7d27439681d62f4e0de1f5e1'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Do extra stuff here

        headers = {'Content-Disposition': 'attachment; filename=student-data.json'}
        return JSONResponse(content=data, headers=headers)

    else:
        return {}


# create the url name for the page
@router.get('/download-csv')
# create a method that will return value you want to the browser to see
def download_csv():
    try:
        aries = current_grades('994', '2020')
        csv_data = aries.get_current_grades_csv_io()

        def iterate(data):
            for row in data:
                yield row.encode()

        return StreamingResponse(iterate(csv_data), media_type='text/csv',
                                 headers={'Content-Disposition': 'attachment; filename="current_grades.csv"'})
    except Exception as e:
        print(e)
        return {}

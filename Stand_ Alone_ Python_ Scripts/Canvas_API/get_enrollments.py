import requests
import os
from dotenv import load_dotenv
from nextUrl import nextUrl

load_dotenv()
CANVAS_API_TOKEN = os.getenv('CANVAS_API_TOKEN')


def get_enrollments(course_id):
    data = []
    canvas_base_url = "https://canvas.instructure.com/api/v1/"
    canvas_api = canvas_base_url + "courses/" + str(course_id) + "/enrollments?type[]=StudentEnrollment"
    response = requests.get(canvas_api, headers={'Authorization': 'Bearer ' + CANVAS_API_TOKEN})

    if response.status_code == 200:
        for enrollment in response.json():
            data.append(enrollment)

        next_url = nextUrl(response.headers['Link'])

        while next_url:
            response = requests.get(next_url, headers={'Authorization': 'Bearer ' + CANVAS_API_TOKEN})
            for enrollment in response.json():
                data.append(enrollment)
            next_url = nextUrl(response.headers['Link'])
        return data

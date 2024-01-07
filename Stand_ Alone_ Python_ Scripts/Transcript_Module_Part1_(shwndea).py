import csv
import json
import numpy as np
import pandas as pd
import random
import requests
import string
from typing import List


def get_transcripts(
        aeries_base_url: str,
        aeries_api_token: str,
        school_code: str,
        student_ids: str,
) -> str:
    """
    Get transcripts from Aries API.
    :param aeries_base_url:
    :param aeries_api_token:
    :param school_code:
    :param student_ids:
    :return:
    """
    data = []
    api_base = f"{aeries_base_url}/api/v5/schools/{school_code}/Transcript/{student_ids}"
    api_base2 = f"{aeries_base_url}api/v5/courses/"
    request_headers = {"formatType": "text/json", "AERIES-CERT": aeries_api_token}
    request = requests.get(api_base, headers=request_headers)
    request2 = requests.get(api_base2, headers=request_headers)
    requesttool = request.json()  # turns request to json request
    requesttool2 = request2.json()  # turns request to json request
    print(requesttool)

    data.append(requesttool2)

    ran_string = ''.join(random.choice(string.ascii_letters) for i in range(10))
    file_path_root = f'Transcripts_{ran_string}'
    file_path = file_path_root + '.csv'  # fix

    with open('All_Course_Grades_in_Transcripts.json', 'w') as Course_Grades_in_Transcripts:
        json.dump(requesttool[0]['CourseGrades'], Course_Grades_in_Transcripts)
        print(type(Course_Grades_in_Transcripts))
    with open('All_Course_Grades_in_Transcripts.json') as json_file:
        a = json.load(json_file)
        with open(file_path, 'w', newline='', ) as enrollment_csv_file:
            header = ['Id', 'SchYear', 'SchID', 'Term', 'ClassN', 'Units', 'GradeAch', 'Class', 'ClassT',
                      'ClassLvl_1/2', 'ClassLvl_2/2', 'A_Gstatus_1/2', 'A_Gstatus_2/2', ]
            csv_writer = csv.writer(enrollment_csv_file)
            csv_writer.writerow(header)

            for manydict in range(len(requesttool[0]['CourseGrades'])):
                c = dict(a[manydict])
                csv_writer.writerow(
                    [student_ids, c['SchoolYear'], c['SchoolTakenName'], c['Term'], c['CourseID'], c['CreditCompleted'],
                     c['Mark'], c['CourseID']])
    # End: Create CSV File
    return print(request)

get_transcripts('https://demo.aeries.net', '477abe9e7d27439681d62f4e0de1f5e1', '994', 'insert student id')

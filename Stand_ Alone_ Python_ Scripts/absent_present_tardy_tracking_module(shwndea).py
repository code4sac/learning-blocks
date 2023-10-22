# phase 2 use the Student Attendance request to track absence day by day /api/v5/schools/{SchoolCode}/attendance/{StudentID}
import csv
import json
import random
import requests
import string
from typing import List


def get_current_grades(
        aeries_base_url: str,
        aeries_api_token: str,
        school_code: str,
        student_ids: str,
        year: str,
) -> str:
    """
    Get current grades for students in school.
    :param aeries_base_url:
    :param aeries_api_token:
    :param school_code:
    :param student_ids:
    :param year:
    :return:
    """
    header = ['StID', 'SchYear', 'SchID', 'Term', 'Abs_ex', 'Abs_unex', 'DaysAtt', 'DaysEnr', 'DaysSuspension',
              'DaysTardy']
    api_base = f"{aeries_base_url}/api/v5/schools/{school_code}/AttendanceHistory/Summary/{student_ids}"
    # api_base = f"{aeries_base_url}/api/v5/enrollment/{student_ids}/year/{year}"

    request_headers = {"formatType": "text/json", "AERIES-CERT": aeries_api_token}
    # random letters
    ran_string = ''.join(random.choice(string.ascii_letters) for i in range(10))
    file_path = f'Absence_{ran_string}.csv'

    with open(file_path, 'w', newline='') as current_grades_csv_file:
        csv_writer = csv.writer(current_grades_csv_file)
        csv_writer.writerow(header)  # header row in the csv

        api_url = f"{api_base}"
        request_json = requests.get(api_url, headers=request_headers).json()
        c = dict(request_json[0])
        # print(type(c['HistoryDetails'][0]))
        # d=dict(c['HistoryDetails'])
        # print(d['StudentID'],d['SchoolYear'],d['SchoolCode'])
        print(header)
        for x in range(len(c['HistorySummaries'])):
            csv_writer.writerow(
                [f'{student_ids}', c['HistorySummaries'][x]['SchoolYear'], c['HistorySummaries'][x]['SchoolCode'],
                 "Please Define term", c['HistorySummaries'][x]['DaysExcused'],
                 c['HistorySummaries'][x]['DaysUnexcused'], c['HistorySummaries'][x]['DaysPresent'],
                 c['HistorySummaries'][x]['DaysEnrolled'], c['HistorySummaries'][x]['DaysSuspension'],
                 c['HistorySummaries'][x]['DaysTardy']])
        # (len(c['HistoryDetails']) is 6 so make a loop to pull all relivent data from nested loop
        # for data in d:
        # csv_writer.writerow(d['SchoolYear'])
        # print(filteredData.keys())

    return file_path


get_current_grades('https://demo.aeries.net/aeries', '477abe9e7d27439681d62f4e0de1f5e1', '994', '99400002', '2022')

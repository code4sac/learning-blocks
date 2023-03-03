import pandas as pd


def aries_report_card(event, context):
    try:
        query_string_parameters = event["queryStringParameters"]
        if query_string_parameters["api_type"] == "production":
            api = aries_api()
        elif query_string_parameters["api_type"] == "demo":
            api = demo_aries_api(school_id=query_string_parameters["school_id"],
                                 student_id=query_string_parameters["student_id"],
                                 api_key=query_string_parameters["api_key"])
        report = api.get_current_grades()
    except requests.RequestException as error:
        raise error
    response = {"statusCode": 200, 'body': report, 'headers': {"Access-Control-Allow-Origin": "*"}}
    return response


def aries_students(event, context):
    try:
        query_string_parameters = event["queryStringParameters"]
        if query_string_parameters["api_type"] == "production":
            api = aries_api()
        elif query_string_parameters["api_type"] == "demo":
            api = demo_aries_api(school_id=query_string_parameters["school_id"],
                                 grade=query_string_parameters["grade"],
                                 api_key=query_string_parameters["api_key"])
        try:
            if query_string_parameters["paged"] > 1:
                report = api.get_autofill_students()
            else:
                report = api.get_all_students()
        except KeyError:
            report = api.get_all_students()
    except requests.RequestException as error:
        raise error
    response = {"statusCode": 200, 'body': report, 'headers': {"Access-Control-Allow-Origin": "*"}}
    return response


class demo_aries_api:
    DEMO_BASE_API_HOST = "https://demo.aeries.net/aeries"

    def __init__(self, school_id: str, api_key: str, student_id: str = "", grade: str = ""):
        """Initialize the API class."""
        self.school_id = school_id
        self.student_id = student_id
        self.grade = grade
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("AERIES_API_KEY environment variable not set.")
        self.request_headers = {
            "formatType": "text/json",
            "AERIES-CERT": self.api_key,
        }

    def get_current_grades(self):
        url = f"{self.DEMO_BASE_API_HOST}/api/v5/schools/{self.school_id}/ReportCard/{self.student_id}"
        response = requests.get(url, headers=self.request_headers)
        return response.json()

    def get_all_students(self):
        url = f"{self.DEMO_BASE_API_HOST}/api/v5/schools/{self.school_id}/students/grade/{self.grade}"
        response = requests.get(url, headers=self.request_headers)
        return response.json()

    def get_autofill_students(self):
        url = f"{self.DEMO_BASE_API_HOST}/api/v5/schools/{self.school_id}/students/grade/{self.grade}"
        response = requests.get(url, headers=self.request_headers)
        df = pd.DataFrame(response.json())
        return df.head().to_json()

    def get_current_grades_csv(self):
        result = ""
        try:
            result = self.make_csv(self.get_current_grades())
        except:
            result = "Creating CSV from JSON failed"
        return result

    def make_csv(self, json_data) -> str:
        csv_file = ""
        ID = ["insert list of IDs here"]
        IDlen = len(ID)
        x = 0
        y = 0
        d = {}
        df = pd.DataFrame(data=d)
        jsonlen = len(json_data)
        z = []
        z1 = []
        z2 = []
        while y < jsonlen:
            z.append(data[y][1]['StudentID'])
            z1.append(data[y][1]['LeaveDate'])
            z2.append(data[y][1]['ExitReasonCode'])
            # data[y][1]['StudentID']
            # data[y][1]['LeaveDate']
            y += 1
        df = pd.DataFrame(z)
        df.to_csv('StudentID(ExtReason).csv', header=['StudentID'], index=False)
        data_new = pd.read_csv('filename.csv')
        data_new['EndDate'] = z1
        data_new.to_csv('StudentID&EndDate(ExtReason).csv')
        data_new['ExitReasonCode'] = z2
        data_new.to_csv('StudentID&EndDate&ExitReasonCode.csv')
        return csv_file


import csv
import os

import requests


class aries_api:
    BASE_API_HOST = "https://aeries.gcccharters.org/Admin/api/v5"

    # "InsertSTUIDNum" "

    def __init__(self, school_id: str, item_id: str):
        """Initialize the API class."""
        self.school_id = school_id
        self.item_id = item_id
        self.api_key = os.environ.get("AERIES_API_KEY")
        if not self.api_key:
            raise ValueError("AERIES_API_KEY environment variable not set.")
        self.request_headers = {
            "formatType": "text/json",
            "AERIES-CERT": self.api_key,
        }

    def get_current_grades(self):
        url = f"{self.BASE_API_HOST}/schools/{self.school_id}/{self.item_id}"
        response = requests.get(url, headers=self.request_headers)
        print(response.text)
        return response.json()

    def get_current_grades_csv(self):
        val = self.get_current_grades()
        with open("current_grades.csv", "w") as f:
            w = csv.writer(f)
            w.writerow(val.keys())
            w.writerow(val.values())

    #  def get_current_grades(self):
    #      """Get the current grades from the Aeries API."""
    #      request = requests.get(self.API_HOST, headers=self.request_headers)
    #      val = request.json()
    #      return val
    #
    #  def get_current_grades_csv(self):

    #
    #  with open('Current_Grades.json', 'w') as enrollment_json_file:
    #      json.dump(requesttool, enrollment_json_file)
    #  with open('Current_Grades.csv', 'w', newline='') as enrollment_csv_file:
    #    csv_writer = csv.writer(enrollment_csv_file)
    #    columns_to_include = [
    #      'StudentID',
    #      'StudentReportCardCourses'
    #
    #
    #    ]
    #    csv_writer.writerow(columns_to_include)
    #
    #
    #    for data in requesttool:
    #        filteredData = dict((k, data[k]) for k in columns_to_include if k in data)
    #        x = len(filteredData['StudentReportCardCourses'])
    #        csv_writer.writerow(filteredData.values())
    #
    #        for i in range(x):
    #            csv_writer.writerow(filteredData['StudentReportCardCourses'][0].keys())
    #            csv_writer.writerow(filteredData['StudentReportCardCourses'][i].values())
    #            w = filteredData['StudentReportCardCourses'][0]['MarkingPeriodGrades'][0].keys()
    #            v= set(filteredData['StudentReportCardCourses'][0]['MarkingPeriodGrades'][0].keys())
    #            csv_writer.writerow(filteredData['StudentReportCardCourses'][0]['MarkingPeriodGrades'][0].keys())
    #            csv_writer.writerow(filteredData['StudentReportCardCourses'][i]['MarkingPeriodGrades'][0].values())
    #
    #
    #  #print(filteredData['StudentReportCardCourses'][0]['MarkingPeriodGrades'][0]['Hours'])

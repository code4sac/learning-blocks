import csv
import os

import requests


class Api:
    BASE_API_HOST = "https://demo.aeries.net/api/v5"
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

import pandas as pd
import requests


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

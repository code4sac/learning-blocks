
import csv
# import io
# import os

import requests


class students_status:
    BASE_API_HOST = "https://demo.aeries.net/aeries/api/v5"

    # args school id

    def __init__(self):
        """Initialize the API class."""

        self.school_id = 994
        # self.api_key = os.environ.get("AERIES_API_KEY")
        self.api_key = '477abe9e7d27439681d62f4e0de1f5e1'
        if not self.api_key:
            raise ValueError("AERIES_API_KEY environment variable not set.")
        self.request_headers = {
            "formatType": "text/json",
            "AERIES-CERT": self.api_key,
        }

    def get_students_by_status(self):

        url = f"{self.BASE_API_HOST}/schools/{self.school_id}/students?cert={self.api_key}&EndingRecord=5&StartingRecord=0"
        try:
            response = requests.get(url, headers=self.request_headers, timeout=10)
            extracted_data = []

            if response.status_code == 200:
                data = response.json()
                keys_needed = ['StudentID', 'Grade',
                            'AttendanceProgramCodePrimary', 'InactiveStatusCode']
                for obj in data[:len(data)]:
                    filtered_obj = {key: obj[key] for key in keys_needed}
                    extracted_data.append(filtered_obj)

            return extracted_data
        except requests.exceptions.RequestException as err:
            print("API request failed:" + str(err))
            return []

    def export_students_by_status_csv(self):
        val = self.get_students_by_status()
        col_names = val[0].keys()

        with open("students_by_status.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=col_names)
            w.writeheader()
            w.writerows(val)

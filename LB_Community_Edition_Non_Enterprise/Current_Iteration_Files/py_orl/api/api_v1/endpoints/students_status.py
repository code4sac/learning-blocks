import csv
import json

import pandas as pd
import requests


class students_status:
    BASE_API_HOST = 'https://demo.aeries.net/aeries/api/v5'

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

        url = f"{self.BASE_API_HOST}/schools/{self.school_id}/students?cert={self.api_key}&EndingRecord=50&StartingRecord=0"
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
        values = self.get_students_by_status()
        col_names = values[0].keys()

        with open("students_by_status.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=col_names)
            w.writeheader()
            w.writerows(values)

    def generate_table_number_students(self):
        df = pd.DataFrame(self.get_students_by_status())

        result = df.groupby(['Grade', 'AttendanceProgramCodePrimary', 'InactiveStatusCode']).size().reset_index(
            name='Count')

        pivot_table = result.pivot_table(index=['Grade', 'AttendanceProgramCodePrimary'], columns='InactiveStatusCode',
                                         values='Count', fill_value=0)

        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)

        print(pivot_table)

    def export_students_by_status_json(self):
        values = json.dumps(self.get_students_by_status(), indent=4)

        with open("students_by_status.json", "w") as json_file:
            json_file.write(values)

# TO TEST BEHAVIOR
# smth = students_status()
# smth.export_students_by_status_json()

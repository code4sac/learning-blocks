import csv
import random
import string

import requests

columns_to_include = ["StudentID", "LeaveDate", "ExitReasonCode"]


def get_current_grades(
    aeries_base_url: str,
    aeries_api_token: str,
    school_code: str,
    student_ids: list[str],
    academic_year: int,
) -> str:
    api_base = f"{aeries_base_url}/Admin/api/v5/schools/{school_code}/enrollment"
    # api_base = f'/Admin/api/v5/schools/{schoolcode}/enrollment/{StudentID}/year/{AcademicYear}'
    request_headers = {"formatType": "text/json", "AERIES-CERT": aeries_api_token}
    # random letters
    ran_string = "".join(random.choice(string.ascii_letters) for _ in range(10))
    file_path = f"Exit_Reason_{ran_string}.csv"

    with open(file_path, "w", newline="") as current_grades_csv_file:
        csv_writer = csv.writer(current_grades_csv_file)
        csv_writer.writerow(columns_to_include)  # header row in the csv

        for student_id in student_ids:
            api_url = f"{api_base}/{student_id}/year/{academic_year}"
            request_json = requests.get(api_url, headers=request_headers).json()

            for data in request_json:
                filteredData = dict(
                    (k, data[k]) for k in columns_to_include if k in data
                )
                csv_writer.writerow(filteredData.values())

    return file_path

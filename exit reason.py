from typing import List
import requests
import string
import random
import csv

columns_to_include = [
'StudentID',
'LeaveDate',
'ExitReasonCode'
]

def get_current_grades(
    aeries_base_url: str,
    aeries_api_token: str,
    school_code: str,
    student_ids: list[str]
) -> str:
  api_base = "%s/Admin/api/v5/schools/%s/enrollment" % aeries_base_url, school_code
  request_headers = {"formatType":"text/json", "AERIES-CERT": aeries_api_token}
  # random letters
  ran_string = ''.join(random.choice(string.ascii_letters) for i in range(10))
  file_path = 'Exit_Reason_%s.csv' % ran_string

  with open(file_path, 'w', newline='') as current_grades_csv_file:
    csv_writer = csv.writer(current_grades_csv_file)
    csv_writer.writerow(columns_to_include) # header row in the csv
    
    for student_id in student_ids:
      api_url = "%s/%s" % api_base, student_id
      request_json = requests.get(api_url, headers = request_headers).json()
      
      for data in request_json:
        filteredData = dict((k, data[k]) for k in columns_to_include if k in data)
        x = len(filteredData['LeaveDate'])
        csv_writer.writerow(filteredData.values())

        for i in range(x):
            csv_writer.writerow(filteredData[i][1]['StudentID'])
            csv_writer.writerow(filteredData[i][1]['LeaveDate'])
            csv_writer.writerow(filteredData[i][1]['ExitReasonCode'])

  
  return file_path


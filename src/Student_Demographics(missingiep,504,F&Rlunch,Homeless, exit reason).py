from typing import List
import requests
import string
import random
import csv

columns_to_include = [
      'StudentID',
      'ProgramCode',
      'ProgramDescription',
      'EligibilityStartDate',
      'EligibilityEnddate',
      'ExtendedProperties'
]

def Student_Enrollmet_I5LH(
    aeries_base_url: str,
    aeries_api_token: str,
    school_code: str,
    student_ids: str,
 
) -> str:
  api_base = f"{aeries_base_url}/api/v5/schools/{school_code}/students"
  #api_base = f'/Admin/api/v5/schools/{schoolcode}/enrollment/{StudentID}/year/{AcademicYear}'
  request_headers = {"formatType":"text/json", "AERIES-CERT": aeries_api_token}
  # random letters
  ran_string = ''.join(random.choice(string.ascii_letters) for i in range(10))
  file_path = f'Student_Enrollment_(iep,504,F&Rlunch,Homeless){ran_string}.csv'

  with open(file_path, 'w', newline='') as Student_Enrollment_csv_file:
    csv_writer = csv.writer(Student_Enrollment_csv_file)
    csv_writer.writerow(columns_to_include) # header row in the csv
   
 
    api_url = f"{api_base}/{student_ids}/programs"
    request_json = requests.get(api_url, headers = request_headers).json()
    print(request_json)
    for data in request_json:
      filteredData = dict((k, data[k]) for k in columns_to_include if k in data)
      csv_writer.writerow(filteredData.values())
       

  
  return file_path
Student_Enrollmet_I5LH('https://demo.aeries.net/aeries/','477abe9e7d27439681d62f4e0de1f5e1','994','99400002')

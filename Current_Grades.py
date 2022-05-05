import numpy as np
import requests
import json
import pandas as pd
import csv


API_HOST = "https://aeries.gcccharters.org/Admin/api/v5/schools/815/ReportCard/980047317"

requestHeaders = {"formatType":"text/json", \
					 "AERIES-CERT":"[INSERT API KEY]"}


request = requests.get(API_HOST, headers = requestHeaders)
requesttool = request.json() 

with open('Current_Grades.json', 'w') as enrollment_json_file:
    json.dump(requesttool, enrollment_json_file)
with open('Current_Grades.csv', 'w', newline='') as enrollment_csv_file:
  csv_writer = csv.writer(enrollment_csv_file)
  columns_to_include = [
    'StudentID',
    'StudentReportCardCourses'
    
   
  ]
  csv_writer.writerow(columns_to_include)
  

  for data in requesttool:
      filteredData = dict((k, data[k]) for k in columns_to_include if k in data)
      x = len(filteredData['StudentReportCardCourses'])
      csv_writer.writerow(filteredData.values())

      for i in range(x):
          csv_writer.writerow(filteredData['StudentReportCardCourses'][0].keys())
          csv_writer.writerow(filteredData['StudentReportCardCourses'][i].values())
          w = filteredData['StudentReportCardCourses'][0]['MarkingPeriodGrades'][0].keys()
          v= set(filteredData['StudentReportCardCourses'][0]['MarkingPeriodGrades'][0].keys())
          csv_writer.writerow(filteredData['StudentReportCardCourses'][0]['MarkingPeriodGrades'][0].keys())
          csv_writer.writerow(filteredData['StudentReportCardCourses'][i]['MarkingPeriodGrades'][0].values())
              
          
#print(filteredData['StudentReportCardCourses'][0]['MarkingPeriodGrades'][0]['Hours'])

import numpy as np
import requests
import json
import pandas as pd
import csv

# Begin: request information
API_HOST = "https://aeries.gcccharters.org/Admin/api/v5/schools/815/students/0/programs"

requestHeaders = {"formatType":"text/json", \
					 "AERIES-CERT":"[INSERT API KEY]"}


request = requests.get(API_HOST, headers = requestHeaders)
requesttool = request.json() #generates list obj that I can pull fields from

print(request.text)
with open('iep.json', 'w') as iep_json_file:
    json.dump(requesttool, iep_json_file)
    
with open('iep.csv', 'w', newline='') as iep_csv_file:
  csv_writer = csv.writer(iep_csv_file)
  columns_to_include = [
      'StudentID',
      'ProgramCode',
      'ProgramDescription',
      'EligibilityStartDate',
      'EligibilityEnddate',
      'ExtendedProperties'

      ]
  csv_writer.writerow(columns_to_include)

  for data in requesttool:
      filteredData = dict((k, data[k]) for k in columns_to_include if k in data)
      csv_writer.writerow(filteredData.values())

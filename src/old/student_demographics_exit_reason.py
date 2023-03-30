import numpy as np
import requests
import json
import pandas as pd
import csv

# Begin: request information
API_HOST = "https://aeries.gcccharters.org/Admin/api/v5/schools/{insertscholid}/students/grade/{grade}"

requestHeaders = {"formatType":"text/json", \
					 "AERIES-CERT":"[INSERT API KEY]"}


request = requests.get(API_HOST, headers = requestHeaders)
requesttool = request.json() #generates list obj that I can pull fields from

print(request.text)
# End: request information

with open('enrollment.json', 'w') as enrollment_json_file:
    json.dump(requesttool, enrollment_json_file)
with open('enrollment.csv', 'w', newline='') as enrollment_csv_file:
  csv_writer = csv.writer(enrollment_csv_file)
  columns_to_include = [
    'StudentID', 
    'OldStudentID',
    'CorrespondenceLanguageCode',
    'CounselorNumber',
    'StudentPersonalEmailAddress',
    'SchoolCode',
    'StudentNumber',
    'StateStudentID',
    'LastName',
    'FirstName',
    'MiddleName',
    'Gender',
    'Grade',
    'GradeLevelShortDescription',
    'GradeLevelLongDescription',
    'Birthdate',
    'ParentGuardianName',
    'HomePhone',
    'StudentMobilePhone',
    'MailingAddress',
    'MailingAddressCity',
    'MailingAddressState',
    'MailingAddressZipCode',
    'ResidenceAddress',
    'ResidenceAddressCity',
    'ResidenceAddressState',
    'ResidenceAddressZipCode',
    'AddressVerified',
    'EthnicityCode',
    'RaceCode1',
    'SchoolEnterDate',
    'SchoolLeaveDate',
    'DistrictEnterDate',
    'AttendanceProgramCodePrimary',
    'LockerNumber',
    'LowSchedulingPeriod',
    'HighSchedulingPeriod',
    'FamilyKey',
    'LanguageFluencyCode',
    'HomeLanguageCode',
    'ParentEdLevelCode',
    'ParentEmailAddress',
    'StudentEmailAddress',
    'NetworkLoginID',
    'EarlyWarningPoints',
    'HomeRoomTeacherNumber',
    'NotificationPreferenceCode',
    'NextSchoolCode',
    'NextGrade',
    'NextGradeLevelShortDescription',
    'NextGradeLevelLongDescription'
  ]
  csv_writer.writerow(columns_to_include)

  for data in requesttool:
      filteredData = dict((k, data[k]) for k in columns_to_include if k in data)
      csv_writer.writerow(filteredData.values())
      

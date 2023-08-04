from typing import List
import numpy as np
import requests
import json
import pandas as pd
import csv
import random
import string

def get_transcripts2(
    aeries_base_url: str,
    aeries_api_token: str,
    school_code: str,
    student_ids: str,
    courses: list,
) -> str:
  
    header =['Class','ClassT','ClassLvl_1/2','ClassLvl_2/2','A_Gstatus_1/2','A_Gstatus_2/2']
    Courseslen = len(f"{courses}")
    data = []
    ran_string = ''.join(random.choice(string.ascii_letters) for i in range(10))
    file_path = f'Transcripts_2_of_2_{ran_string}.csv'
    with open(file_path, 'w', newline='') as Transcripts_2_of_2_csv_file:
        csv_writer = csv.writer(Transcripts_2_of_2_csv_file)
        csv_writer.writerow(header)
        for x in range(Courseslen):
            Course = str(f"{courses[x]}")
            API_HOST = "https://demo.aeries.net/api/v5/courses/" + Course
            requestHeaders = {"formatType":"text/json", \
                              "AERIES-CERT":"cf919ece752842fd83d7edfdf3ac7bb9"}
            request = requests.get(API_HOST, headers = requestHeaders)
            requesttool = request.json()
            data.append(requesttool)
            with open('Transcripts_2_of_2.json', 'w') as enrollment_json_file:
                json.dump(data, enrollment_json_file)
            with open('Transcripts_2_of_2.json') as json_file:
                a = json.load(json_file)
            for manydict in range(len(a)):
                c= dict(a[manydict])
            csv_writer.writerow([c['ID'],c['LongDescription'],c['NonAcademicOrHonorsCode'],c['CollegePrepIndicatorCode'],c['CSU_SubjectAreaCode'],c['UC_SubjectAreaCode']])
            print(c.keys())
            print(c.values())    

    return file_path


        

get_transcripts2('https://demo.aeries.net/aeries','477abe9e7d27439681d62f4e0de1f5e1','990','99400002',    courses=['insert list of courses'])

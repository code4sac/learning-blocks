from typing import List
import numpy as np
import requests
import json
import pandas as pd
import csv
import random
import string

def get_transcripts_2(
    aeries_base_url: str,
    aeries_api_token: str,
) -> str:
    courses=[
'000',
'000001',
'00000K',
'0001',
'1',
'1-2',
'10',
'10152',
'11',
'110005',
'110006',
'110007',
'110050',
'112005',
'115045',
'115050',
'12',
'120006',

]
    header =['Class','ClassT','ClassLvl_1/2','ClassLvl_2/2','A_Gstatus_1/2','A_Gstatus_2/2']
    Courseslen = len(courses)
    data = []
    ran_string = ''.join(random.choice(string.ascii_letters) for i in range(10))
    file_path = f'Transcripts_2_of_2_{ran_string}.csv'
    with open(file_path, 'w', newline='') as Transcripts_2_of_2_csv_file:
        csv_writer = csv.writer(Transcripts_2_of_2_csv_file)
        csv_writer.writerow(header)
        for x in range(Courseslen):
            Course = str(courses[x])
            API_HOST = "https://aeries.gcccharters.org/Admin/api/v5/courses/" + Course
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


        

get_transcripts_2('https://aeries.gcccharters.org','cf919ece752842fd83d7edfdf3ac7bb9')

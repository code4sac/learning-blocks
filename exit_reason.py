

import numpy as np
import requests
import json
import pandas as pd
import csv

ID = ["insert list of IDs here"]
IDlen = len(ID)
x = 0
y = 0
data = []
d = {}
df = pd.DataFrame(data=d)

while x < IDlen:
    stdID = str(ID[x])
    API_HOST = "https://aeries.gcccharters.org/Admin/api/v5/schools/815/enrollment/" + stdID
    requestHeaders = {"formatType":"text/json", \
					 "AERIES-CERT":"insert Key here"}
    request = requests.get(API_HOST, headers = requestHeaders)
    requesttool = request.json()
    data.append(requesttool)
    x +=1
with open('exit_reason.json', 'w') as exit_reason_json_file:
    json.dump(data, exit_reason_json_file)
with open('exit_reason.json') as json_file:
    data = json.load(json_file)
    jsonlen = len(data)
    z=[]
    z1=[]
    z2=[]
    while y < jsonlen:
        z.append(data[y][1]['StudentID'])
        z1.append(data[y][1]['LeaveDate'])
        z2.append(data[y][1]['ExitReasonCode'])
#data[y][1]['StudentID']
#data[y][1]['LeaveDate']
        y+=1
df = pd.DataFrame(z)
df.to_csv('StudentID(ExtReason).csv', header= ['StudentID'],index=False)
data_new = pd.read_csv('filename.csv')
data_new['EndDate'] = z1
data_new.to_csv('StudentID&EndDate(ExtReason).csv')
data_new['ExitReasonCode'] = z2
data_new.to_csv('StudentID&EndDate&ExitReasonCode.csv') 

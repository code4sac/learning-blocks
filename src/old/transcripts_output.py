import requests
import json
API_HOST = "https://delnorte.asp.aeries.net/admin/api/v3/schools/520/students/grade/11"
requestHeaders = {"formatType":"application/json", \
					 "AERIES-CERT":"insert cert key here"}

#DEMO API: 477abe9e7d27439681d62f4e0de1f5e1
#DOCUMENTATION: https://support.aeries.com/support/solutions/articles/14000077926-aeries-api-full-documentation#aeries-api-h5
def reqpull():
    request = requests.get(API_HOST, headers = requestHeaders)
    r1= request.json()

    
 
    q=[]
    a=[]
    for q in r1:
        a.append(q['PermanentID'])
    print("The Permenant ID's for this grade level are")
    print(a)
    #if you want just the perm ID's delete below
    for i  in a:
        API_HOST1 = "https://delnorte.asp.aeries.net/admin/api/v3/schools/520/Transcript/"+x
        requestHeaders1={"formatType":"application/json", \
					 "AERIES-CERT":"insert vert key here"}
        request1 = requests.get(API_HOST1, headers = requestHeaders1)
        r2= request1.json()
        print("Printing each transcript may take a while so i am going to make it better")
        print(r2)
        
       





#dont delete below this
reqpull()

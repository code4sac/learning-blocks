from .current_grades import get_current_grades
import requests
import json

def test_current_grades():
  # aeries_base_url='https://demo.aeries.net/aeries'
  # aeries_api_token='477abe9e7d27439681d62f4e0de1f5e1'
  # school_code='884'
  # api_base = f"{aeries_base_url}/api/v5/schools/994/ReportCard/99400002"
  # request_headers = {"Accept":"application/json", "AERIES-CERT": aeries_api_token}

  # request_json = requests.get(api_base, headers = request_headers).json()
  # # print(list(map(lambda s: s.get('StudentID', None), request_json)))
  # print(json.dumps(request_json, indent=2))

  # School codes [0, 884, 894, 900, 901, 902, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999]
  # 884 student ids: [88400001, 88400002, 88400003, 88400004, 88400005, 88400006, 88400007, 88400008, 88400009, 88400010, 88400011, 88400012, 88400013, 88400014, 88400015]

  get_current_grades(
    aeries_base_url='https://demo.aeries.net/aeries',
    aeries_api_token='477abe9e7d27439681d62f4e0de1f5e1',
    school_code='994',
    student_ids=['99400002'],
  )

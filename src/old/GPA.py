import csv
import json
import requests

# Begin: request information
API_HOST = "https://aeries.gcccharters.org/Admin/api/v5/schools/815/gpas/980047317"

requestHeaders = {"formatType": "text/json", "AERIES-CERT": "INSERT API KEY"}


request = requests.get(API_HOST, headers=requestHeaders)
requesttool = request.json()  # turns request to json request

print(request.text)
# End: request information

# Begin: convert Json to CSV
with open("gpa.json", "w") as enrollment_json_file:
    json.dump(requesttool, enrollment_json_file)
# End: convert JSon to CSV
# Begin: saving the csv file
with open("gpa.csv", "w", newline="") as enrollment_csv_file:
    csv_writer = csv.writer(enrollment_csv_file)
    columns_to_include = [
        "StudentID",
        "SchoolCode",
        "ClassRank",
        "ClassSize",
        "ClassRank1012",
        "GPA_CumulativeAcademic",
        "GPA_CumulativeTotal",
        "GPA_CumulativeAcademic1012",
        "GPA_CumulativeAcademicNonWeighted",
        "GPA_CumulativeTotalNonWeighted",
        "GPA_CumulativeAcademic1012NonWeighted",
        "GradePointsCumulative",
        "GPA_UC_Preliminary",
        "GPA_CSU_Preliminary",
        "GPA_CumulativeCitizenship",
        "GPA_GradeReportingCitizenship",
        "CreditsAttempted",
        "CreditsCompleted",
        "GPA_GradeReportingAcademic",
        "GPA_GradeReportingTotal",
        "GPA_GradeReportingAcademicNonWeighted",
        "GPA_GradeReportingTotalNonWeighted",
        "GradeReportingClassRank",
        "GradeReportingClassSize",
        "GradeReportingCreditsAttempted",
        "GradeReportingCreditsCompleted",
    ]
    csv_writer.writerow(columns_to_include)

    for data in requesttool:
        filteredData = dict((k, data[k]) for k in columns_to_include if k in data)
        csv_writer.writerow(filteredData.values())

# End: saving the csv file

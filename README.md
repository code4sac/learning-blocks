# school-grant-data

## Problem Statement

Grant programs have a need to report to the government on their students.  They have a need to gather data from school districts in order to form the reports.  There are a few systems in schools that are used to gather this inforation like PowerSchool and Aeries.  We need to use their apis to programmatically gather this information into csv format so that it can be used to generate reports in Cobro Compass.

## Aeries

Requires a data agreement followed by generating an API key in order to get access to their system.

Aeries has a "sandbox" mode that allows development without accessing to sensitive data.
 
 How to build a request: https://support.aeries.com/support/solutions/articles/14000113681-aeries-api-building-a-request
 Aeries API Documentation: https://support.aeries.com/support/solutions/14000072323
## PowerSchool
 No sandbox but working on getting documentation from a PowerSchool Affiliated firm
## Alma
 Alma has a sandbox that you can mess around with, documentation can be found at: https://developers.exlibrisgroup.com/alma/apis/
## Sensitivities

The apis provide access to data that has PII.  We need to be very sensitive of this data and not download it.  Ideally developer only have access to a sandbox and never have access to sensitive data.  The end users of this tool should be the only ones with sensitive data access.



## If you have any question feel free to email shwndea@gmail.com

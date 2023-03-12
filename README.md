                                                                  ### SCHOOL_GRANT_DATA##

## Problem Statement

Grant programs have a need to report to the government on their students.  They have a need to gather data from school districts in order to form the reports.  There are a few systems in schools that are used to gather this inforation like PowerSchool and Aeries.  We need to use their apis to programmatically gather this information into csv format so that it can be used to generate reports in Cobro Compass.

# CURRENT PROGRESS Last update: 3/11/23. 

This project has moved into a web based service, with the intent of using a Vue.js version 3 front-end and a python back end.  For documentation on Vue.js sign up to:

FRONT-END DOCUMENTATION:
-"Introduction to Vue 3"  at https://frontendmasters.com/courses/vue-3/ 

-"Vue js + Python" at https://www.youtube.com/watch?v=uSawG4dxx2k

-"Host your Python Static site for FREE with Netlify" at https://www.youtube.com/watch?v=UcMnJOsMYuM


Hold demo data in the front end title it "json" so that we can query it. How do you save it to local storage or check if it is already in cache. Maybe create a method to but random lettering at teh end of the name of the file so that you wouldnt have to keep checking cache. This would mean the user would have to delete their cache more often.

BACK-END DOCUMENTATION:
- How to build a request: https://support.aeries.com/support/solutions/articles/14000113681-aeries-api-building-a-request
- Aeries API Documentation: https://support.aeries.com/support/solutions/14000072323

# CURRENT PROGRESS Last update: 3/11/23.

                                                                ### Studen Information Systems ###


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



## If you have any question feel free to email shwndea@gmail.com || NATE  || DAVID

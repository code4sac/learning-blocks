# Learning Blocks Technical Design Doc MVP

MVP without login

Web application with an initial form:

- Aeries Api token
- School code (up to 10)
- List of student id numbers (up to ~500 per school)
- Generate and Download Report Button

Front-end web form can be built using a javascript framework like react or vue.js.  This might not be needed for the initial mvp though as just a simple html web form and a redirect (without javascript) may just work on its own.


Form submission calls or redirects the user to /generate-reports
I recommend building this as an mvp in flask or fastapi -- Django may be a bit too big and clunky for this MVP

User receives a zip of csv/spreadsheet reports that downloads
- Demographics
- Current Grades
- GPA
- Test Scores
- Guardian Contact
- Teacher Name

Future iterations
- Provide a user login and portal to access student reports and analytics
- Would be good to run analytics on the student data that is received in the reports
  - Decision tree
    - If students used specific services, what might the outcomes look like
  - Correlation analysis
    - If there’s a correlation between students who used services and got a specific outcome
  - Comparative Studies
    - Types of services provided (i.e. study skill vs number of absences)
    - Outcome

from datetime import datetime
from sqlalchemy.orm import Session
import crud
import schemas
from core.config import settings


def init_db(db: Session) -> None:
    """
    Initialize the database.
    Default options can include:
    ```python
       name='First Example School'
    ```
    """


academic_session_instance = crud.crud_academic_session.crud_academicsession.get_by_sourcedId(
    db, sourcedId=settings.example_school
)
if not academic_session_instance:
    academic_session_data = {
        "sourcedId": '884_F',
        "status": 'active',
        "dateLastModified": "2023-07-11T01:02:25.257Z",
        "title": 'Fall',
        "type": 'term',
        "startDate": '2023-07-03',
        "endDate": '2023-12-21',
        "parentSourcedId": '884_Y',  # Replace with actual parent sourcedId
        "schoolYear": '2024',
        "schoolSourcedId": settings.example_school,  # Replace with actual school sourcedId
        "parent": {
            "sourcedId": '884_Y',  # Replace with actual parent sourcedId
            "href": "~/ims/oneroster/v1p1/academicSessions/884_Y",  # Replace with actual parent href
            "type": "academicSession",  # Replace with actual parent type
            # Include other parent data fields
        },
        "children": [
            {
                "sourcedId": '884_1',  # Replace with actual child1 sourcedId
                "href": "~/ims/oneroster/v1p1/academicSessions/884_1",  # Replace with actual child1 href
                "type": "academicSession",  # Replace with actual child1 type
                # Include other child1 data fields
            },
            {
                "sourcedId": '884_2',  # Replace with actual child2 sourcedId
                "href": "~/ims/oneroster/v1p1/academicSessions/884_2",  # Replace with actual child2 href
                "type": "academicSession",  # Replace with actual child2 type
                # Include other child2 data fields
            },
            # Add more children if needed
        ],
        # Add any additional fields if needed
    }

    academic_session_instance_in = schemas.AcademicSessionCreate(**academic_session_data)
    academic_session_instance = crud.crud_academic_session.crud_academicsession.create_with_sourcedId(db,
                                                                                                      obj_in=academic_session_instance_in)

category_instance = crud.crud_category.get_by_sourcedId(db, sourcedId=settings.example_category)
metadata = "metadata"
if not category_instance:
    category_data = {
        "sourcedId": "1000335_S",
        "status": "active",
        "dateLastModified": "2012-08-15T16:24:19.000Z",
        "title": "Studio Work",
        ("%s" % metadata): {
            "classId": "994_6100",
            "classes": [
                {"sourcedId": "994_6100"},
                {"sourcedId": "994_6145"}
            ],
            "orgId": 994,
            "termId": "",
            "gradingPeriodId": "6",
            "gradingPeriodEndDate": "2024-01-17",
            "gradingPeriodStartDate": "2023-08-04",
            "gradingPeriodDescription": "IB Vis Art HL I"
        }
    }

    category_instance_in = schemas.CategoryCreate(**category_data)
    category_instance = crud.crud_category.create(db, obj_in=category_instance_in)

# Generated for: crud.class_ in file: models.class_.py
class_instance = crud.crud_class.get_by_sourcedId(db, sourcedId=settings.example_school)
if not class_instance:
    class_data = {
        "title": "AP Statistics",
        "classCode": None,
        "classType": "scheduled",
        "location": "S1",
        "grades": ["11", "12"],
        "subjects": None,
        "course": {
            "href": "~/ims/oneroster/v1p1/courses/0634",
            "sourcedId": "0634",
            "type": "course"
        },
        "school": {
            "href": "~/ims/oneroster/v1p1/orgs/894",
            "sourcedId": "894",
            "type": "org"
        },
        "terms": [
            {
                "href": "~/ims/oneroster/v1p1/academicSessions/894_Y",
                "sourcedId": "894_Y",
                "type": "academicSession"
            }
        ],
        "subjectCodes": None,
        "periods": ["P0 (7:05 AM - 7:55 AM)"],
        "resources": None,
        "sourcedId": "894_100",
        "status": "active",
        "dateLastModified": "2023-01-04T21:40:03.277Z",
        metadata: None
    }

    class_instance_in = schemas.ClassCreate(**class_data)
    class_instance = crud.crud_class.create(db, obj_in=class_instance_in)

# Generated for: crud.classresource in file: models.classresource.py
classresource_instance = crud.crud_classresource.get_by_sourcedId(db, sourcedId=settings.example_school)
if not classresource_instance:
    classresource_instance_in = schemas.ClassResourceCreate(
        sourcedId='894_100',  # Replace 'value' with appropriate data
        status='inactive',  # Replace 'value' with appropriate data
        dateLastModified='2023-01-04T21:40:03.277Z',  # Replace 'value' with appropriate data
        title='no longer used',  # Replace 'value' with appropriate data
        classSourcedId='894_100',  # Replace 'value' with appropriate data
        resourceSourcedId='894_100',  # Replace 'value' with appropriate data
    )
    classresource_instance = crud.crud_classresource.create(db, obj_in=classresource_instance_in)

# Generated for: crud.course in file: models.course.py
course_instance = crud.crud_course.get_by_sourcedId(db, sourcedId=settings.example_school)
if not course_instance:
    course_data = {
        "title": "No Zero Period",
        "schoolYear": None,
        "courseCode": "0001",
        "grades": ["09", "10", "11", "12"],
        "subjects": None,
        "org": {
            "href": "~/ims/oneroster/v1p1/orgs/0",
            "sourcedId": "0",
            "type": "org"
        },
        "subjectCodes": None,
        "resources": None,
        "sourcedId": "0001",
        "status": "active",
        "dateLastModified": "2024-01-01T19:49:05.080Z",
        metadata: None
    }

    course_instance_in = schemas.CourseCreate(**course_data)
    course_instance = crud.crud_course.create(db, obj_in=course_instance_in)

# Generated for: crud.courseresource in file: models.courseresource.py
courseresource_instance = crud.crud_classresource.get_by_sourcedId(db, sourcedId=settings.example_school)
if not courseresource_instance:
    courseresource_instance_in = schemas.CourseResourceCreate(
        sourcedId='0',  # Replace 'value' with appropriate data
        status='active',  # Replace 'value' with appropriate data
        dateLastModified='2024-01-01T19:49:05.080Z',  # Replace 'value' with appropriate data
        title='No Zero Period',  # Replace 'value' with appropriate data
        courseSourcedId='894_0001',  # Replace 'value' with appropriate data
        resourceSourcedId='894_100',  # Replace 'value' with appropriate data
    )
    courseresource_instance = crud.crud_classresource.create(db, obj_in=courseresource_instance_in)

# Generated for: crud.demographic in file: models.demographic.py
demographic_instance = crud.crud_demographic.get_by_sourcedId(db, sourcedId=settings.example_school)
if not demographic_instance:
    demographic_instance_in = schemas.DemographicCreate(
        sourcedId='STU_75500001',  # Replace 'value' with appropriate data
        status='active',  # Replace 'value' with appropriate data
        dateLastModified='2024-01-01T10:27:53.513Z',  # Replace 'value' with appropriate data
        birthDate='2004-01-15',  # Replace 'value' with appropriate data
        sex='male',  # Replace 'value' with appropriate data
        americanIndianOrAlaskaNative='false',  # Replace 'value' with appropriate data
        asian='false',  # Replace 'value' with appropriate data
        blackOrAfricanAmerican='false',  # Replace 'value' with appropriate data
        nativeHawaiianOrOtherPacificIslander='false',  # Replace 'value' with appropriate data
        white='false',  # Replace 'value' with appropriate data
        demographicRaceTwoOrMoreRaces='false',  # Replace 'value' with appropriate data
        hispanicOrLatinoEthnicity='false',  # Replace 'value' with appropriate data
        countryOfBirthCode=' ',  # Replace 'value' with appropriate data
        stateOfBirthAbbreviation=' ',  # Replace 'value' with appropriate data
        cityOfBirth=' ',  # Replace 'value' with appropriate data
        publicSchoolResidenceStatus=' ',  # Replace 'value' with appropriate data
    )
    demographic_instance = crud.crud_demographic.create(db, obj_in=demographic_instance_in)

# Generated for: crud.enrollment in file: models.enrollment.py
enrollment_instance = crud.crud_enrollment.get_by_sourcedId(db, sourcedId=settings.example_school)
enrollment_instance_in = schemas.EnrollmentCreate(
    sourcedId='894_STU_89400001_1038',
    status='active',
    dateLastModified='2023-07-11T01:02:36.377Z',
    classSourcedId='894_1038',
    schoolSourcedId='894',
    userSourcedId='STU_89400001',
    role='student',
    primary='false',
    beginDate='2024-01-30',
    endDate='2024-08-03',
    user={
        "href": "~/ims/oneroster/v1p1/users/STU_89400001",
        "sourcedId": "STU_89400001",
        "type": "user"
    },
    class_={ "href": "~/ims/oneroster/v1p1/classes/894_1038", "sourcedId" :"894_1038", "type": "class" },
    school={
        "href": "~/ims/oneroster/v1p1/orgs/894",
        "sourcedId": "894",
        "type": "org"
    },
    metadata=None  # You can add metadata if needed
    )

    enrollment_instance = crud.crud_enrollment.create(db, obj_in=enrollment_instance_in)



# Generated for: crud.lineitem in file: models.lineitem.py
lineitem_instance = crud.crud_lineitem.get_by_sourcedId(db, sourcedId=settings.example_school)

if not lineitem_instance:
    lineitem_data = {
        "title": "Chapter 12 Test",
        "description": "",
        "assignDate": "2024-03-22T07:00:00.000Z",
        "dueDate": "2024-03-22T07:00:00.000Z",
        "class": {
            "href": "~/ims/oneroster/v1p1/classes/994_5151",
            "sourcedId": "994_5151",
            "type": "class"
        },
        "category": {
            "href": "~/ims/oneroster/v1p1/categories/4326169_T",
            "sourcedId": "4326169_T",
            "type": "category"
        },
        "gradingPeriod": {
            "href": "~/ims/oneroster/v1p1/academicSessions/994_S",
            "sourcedId": "994_S",
            "type": "academicSession"
        },
        "resultValueMin": 0.0,
        "resultValueMax": 60.0000,
        "sourcedId": '0001ABB4-7392-4E79-ADC7-449670651BF0',  # Replace with an appropriate sourcedId
        "status": 'active',  # Replace with the appropriate status
        "dateLastModified": '2023-07-11T01:04:20.070Z',  # Replace with the appropriate dateLastModified
        metadata: {
            "vendorId": ""  # Replace with the appropriate vendorId if needed
        }
    }

    lineitem_instance_in = schemas.LineItemCreate(**lineitem_data)
    lineitem_instance = crud.crud_lineitem.create(db, obj_in=lineitem_instance_in)

# Generated for: crud.org in file: models.org.py
org_instance = crud.crud_org.get_by_sourcedId(db, sourcedId=settings.example_school)

if not org_instance:
    org_instance_in = schemas.OrgCreate(
        sourcedId='0',  # Replace with the appropriate sourcedId
        status='active',  # Replace with the appropriate status
        dateLastModified='2024-01-02T05:12:24.927Z',  # Replace with the appropriate dateLastModified
        name='Eagle Unified School District',  # Replace with the appropriate name
        type='district',  # Replace with the appropriate type
        identifier=None,  # Set to None or replace with the appropriate identifier
        parentSourcedId=None,  # Set to None or replace with the appropriate parentSourcedId
        children=[  # Add child organization data as needed
            {
                "href": "~/ims/oneroster/v1p1/orgs/995",
                "sourcedId": "995",
                "type": "org"
            },
            {
                "href": "~/ims/oneroster/v1p1/orgs/993",
                "sourcedId": "993",
                "type": "org"
            },
            # Add more child organizations if needed
        ]
    )
    org_instance = crud.crud_org.create(db, obj_in=org_instance_in)


# Generated for: crud.resource in file: models.resource.py
resource_instance = crud.resource.get_by_sourcedId(db, sourcedId=settings.example_school)
if not resource_instance:
    resource_instance_in = schemas.ResourceCreate(
        sourcedId='994_X0',  # Replace 'value' with appropriate data
        status='inactive',  # Replace 'value' with appropriate data
        dateLastModified='2024-01-02T05:12:24.927Z',  # Replace 'value' with appropriate data
        vendorResourceId='994_X1',  # Replace 'value' with appropriate data
        title='IDK',  # Replace 'value' with appropriate data
        roles='guardian',  # Replace 'value' with appropriate data
        importance='primary',  # Replace 'value' with appropriate data
        vendorId='994_X2',  # Replace 'value' with appropriate data
        applicationId='994_X3',  # Replace 'value' with appropriate data
    )
    resource_instance = crud.resource.create(db, obj_in=resource_instance_in)

# Generated for: crud.result in file: models.result.py
result_instance = crud.result.get_by_sourcedId(db, sourcedId=settings.example_school)
if not result_instance:
    result_instance_in = schemas.ResultCreate(
        sourcedId='994_X4',  # Replace 'value' with appropriate data
        status='active',  # Replace 'value' with appropriate data
        dateLastModified='2024-01-02T05:12:24.927Z',  # Replace 'value' with appropriate data
        lineItemSourcedId='994_X5',  # Replace 'value' with appropriate data
        studentSourcedId='994_X6',  # Replace 'value' with appropriate data
        scoreStatus='994_X7',  # Replace 'value' with appropriate data
        score='994_X8',  # Replace 'value' with appropriate data
        scoreDate='994_X9',  # Replace 'value' with appropriate data
        comment='994_X10',  # Replace 'value' with appropriate data
    )
    result_instance = crud.result.create(db, obj_in=result_instance_in)

# Generated for: crud.user in file: models.user.py
# Generated for: crud.user in file: models.user.py
user_instance = crud.crud_user.get_by_sourcedId(db, sourcedId=settings.example_school)
if not user_instance:
    user_instance_in = schemas.UserCreate(
        sourcedId='PAT_1',  # Replace 'PAT_1' with the sourcedId value from the JSON data
        status='active',  # Replace 'active' with the status value from the JSON data
        dateLastModified='2022-03-21T19:06:28.507Z',  # Replace with the dateLastModified value
        enabledUser='true',  # Replace with the enabledUser value
        role='parent',  # Replace with the role value
        username='parent@aeries.com',  # Replace with the username value
        userIds=None,  # Replace with the userIds value
        givenName='Adam',  # Replace with the givenName value
        familyName='Abbott',  # Replace with the familyName value
        middleName='',  # Replace with the middleName value
        identifier='0_PAT_1',  # Replace with the identifier value
        email='parent@aeries.com',  # Replace with the email value
        sms=None,  # Replace with the sms value
        phone='',  # Replace with the phone value
        grades=None,  # Replace with the grades value
        password=None,  # Replace with the password value
        orgs=[
            {
                "href": "~/ims/oneroster/v1p1/orgs/894",
                "sourcedId": "894",
                "type": "org"
            },
            {
                "href": "~/ims/oneroster/v1p1/orgs/990",
                "sourcedId": "990",
                "type": "org"
            },
            {
                "href": "~/ims/oneroster/v1p1/orgs/994",
                "sourcedId": "994",
                "type": "org"
            }
        ],  # Replace with the orgs value
        agents=[
            {
                "href": "~/ims/oneroster/v1p1/users/STU_89400001",
                "sourcedId": "STU_89400001",
                "type": "user"
            },
            {
                "href": "~/ims/oneroster/v1p1/users/STU_89400002",
                "sourcedId": "STU_89400002",
                "type": "user"
            },
            {
                "href": "~/ims/oneroster/v1p1/users/STU_89401707",
                "sourcedId": "STU_89401707",
                "type": "user"
            },
            {
                "href": "~/ims/oneroster/v1p1/users/STU_99000004",
                "sourcedId": "STU_99000004",
                "type": "user"
            },
            {
                "href": "~/ims/oneroster/v1p1/users/STU_99000007",
                "sourcedId": "STU_99000007",
                "type": "user"
            },
            {
                "href": "~/ims/oneroster/v1p1/users/STU_99400001",
                "sourcedId": "STU_99400001",
                "type": "user"
            },
            {
                "href": "~/ims/oneroster/v1p1/users/STU_99400002",
                "sourcedId": "STU_99400002",
                "type": "user"
            },
            {
                "href": "~/ims/oneroster/v1p1/users/STU_99401707",
                "sourcedId": "STU_99401707",
                "type": "user"
            }
        ],  # Replace with the agents value
    )
    user_instance = crud.crud_user.create(db, obj_in=user_instance_in)
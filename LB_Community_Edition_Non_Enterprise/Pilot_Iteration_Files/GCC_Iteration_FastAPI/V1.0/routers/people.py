from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session
from models import PeopleInDB
from schemas.schemas import PeopleInDBCreate, PeopleInDBResponse, StudentInDBResponse, TeacherInDBResponse
from databases.databases import get_db  # Ensure relative import is correct

router = APIRouter()

@router.post("/people/", response_model=PeopleInDBResponse)
def create_person(person: PeopleInDBCreate, db: Session = Depends(get_db)):
    try:
        # Insert into the PeopleInDB table using SQLAlchemy Core's text() method
        insert_people_query = text("""
            INSERT INTO people (first_name, last_name, role, sourced_id, enabled_user, date_last_modified, school_code)
            VALUES (:first_name, :last_name, :role, :sourced_id, :enabled_user, :date_last_modified, :school_code)
            RETURNING id, first_name, last_name, role, sourced_id, enabled_user, date_last_modified, school_code
        """)

        result = db.execute(insert_people_query, {
            "FirstName": person.first_name,
            "LastName": person.last_name,
            "Role": person.role,
            "SourcedId": person.sourced_id,
            "EnabledUser": person.enabled_user,
            "DateLastModified": person.date_last_modified,
            "SchoolCode": person.school_code
        })

        db_person = result.fetchone()  # Fetch the inserted row

        if not db_person:
            raise HTTPException(status_code=500, detail="Failed to create person.")

        # Insert the corresponding record based on the role (student or teacher)
        student_data = None
        teacher_data = None

        if person.role == "student":
            insert_student_query = text("""
                INSERT INTO students (id, anonymized_student_ID, anonymized_student_number, sections, schl_associated, birthdate, sourced_ID)
                VALUES (:id, :anonymized_student_ID, :anonymized_student_number, :sections, :schl_associated, :birthdate, :sourced_ID)
                RETURNING id, anonymized_student_ID, anonymized_student_number, sections, schl_associated, birthdate, sourced_ID
            """)

            result = db.execute(insert_student_query, {
                "id": db_person[0],  # Use the id returned from the previous insertion
                "AnonymizedStudentID": person.anonymized_student_ID,
                "AnonymizedStudentNumber": person.anonymized_student_number,
                "Sections": person.sections,
                "SchlAssociated": person.schl_associated,
                "Birthdate": person.birthdate,
                "sourced_ID": person.sourced_ID
                "GradeLevels": person.grade_levels,
            })

            db_student = result.fetchone()

            if not db_student:
                raise HTTPException(status_code=500, detail="Failed to create student.")

            # Construct student response data
            student_data = StudentInDBResponse(
                id=db_student[0],
                anonymizedstudentid=db_student[1],
                anonymizedstudentnumber=db_student[2],
                sections=db_student[3],
                schlassociated=db_student[4],
                birthdate=db_student[5]
            )

        elif person.role == "teacher":
            insert_teacher_query = text("""
                INSERT INTO teachers (id, anonymized_teacher_ID, anonymized_teacher_number, sections, stu_associated, schl_associated, site_duties,
                                      credentials, subjects, siteduties, grade_levels, bd_demo)
                VALUES (:id, :anonymized_teacher_ID, :anonymized_teacher_number, :sections, :stu_associated, :schl_associated, :site_duties,
                        :credentials, :subjects, :siteduties, :grade_levels, :bd_demo)
                RETURNING id, anonymized_teacher_ID, anonymized_teacher_number, sections, stu_associated, schl_associated, site_duties,
                          credentials, subjects, siteduties, grade_levels, bd_demo
            """)

            result = db.execute(insert_teacher_query, {
                "id": db_person[0],  # Use the id returned from the people insertion
                "anonymized_teacher_ID": person.anonymized_teacher_ID,
                "anonymized_teacher_number": person.anonymized_teacher_number,
                "sections": person.sections,
                "stu_associated": person.stu_associated,
                "schlassociated": person.schl_associated,
                "credentials": person.credentials,
                "subjects": person.subjects,
                "siteduties": person.site_duties,
                "GradeLevels": person.grade_levels,
                "bd_demo": person.bd_demo
            })

            db_teacher = result.fetchone()

            if not db_teacher:
                raise HTTPException(status_code=500, detail="Failed to create teacher.")

            # Construct teacher response data
            teacher_data = TeacherInDBResponse(
                id=db_teacher[0],
                anonymizedteacherid=db_teacher[1],
                anonymizedteachernumber=db_teacher[2],
                sections=db_teacher[3],
                stuassociated=db_teacher[4],
                schlassociated=db_teacher[5],
                credentials=db_teacher[6],
                subjects=db_teacher[7],
                siteduties=db_teacher[8],
                GradeLevels=db_teacher[9],
                bddemo=db_teacher[10]
            )

        # Commit the transaction
        db.commit()

        # Construct the response data
        response_person = PeopleInDBResponse(
            id=db_person[0],
            firstname=db_person[1],
            lastname=db_person[2],
            role=db_person[3],
            sourcedid=db_person[4],
            EnabledUser=db_person[5],
            dateLastModified=db_person[6],
            school_code=db_person[7],
            student=student_data,
            teacher=teacher_data
        )

        return response_person

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

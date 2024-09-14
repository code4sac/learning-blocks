from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session
from models.models import PeopleInDB
from schemas.schemas import PeopleInDBCreate, PeopleInDBResponse, StudentInDBResponse, TeacherInDBResponse, StudentInDBCreate
from databases.databases import get_db  # Ensure relative import is correct

router = APIRouter()

# Helper function to insert into `people` table
def insert_person(db, person: PeopleInDBCreate):
    insert_people_query = text("""
        INSERT INTO people (first_name, last_name, role, sourced_id, enabled_user, date_last_modified, school_code)
        VALUES (:FirstName, :LastName, :Role, :SourcedId, :EnabledUser, :DateLastModified, :SchoolCode)
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
    
    return result.fetchone()

# Helper function to insert into `students` table
def insert_student(db, student: StudentInDBCreate, db_person):
    insert_student_query = text("""
        INSERT INTO students (id, anonymized_student_ID, anonymized_student_number, sections, schl_associated, birthdate, sourced_ID, grade_levels)
        VALUES (:id, :AnonymizedStudentID, :AnonymizedStudentNumber, :sections, :SchlAssociated, :birthdate, :SourcedID, :GradeLevels)
        RETURNING id, anonymized_student_ID, anonymized_student_number, sections, schl_associated, birthdate, sourced_ID, grade_levels, school_code
    """)
    
    result = db.execute(insert_student_query, {
        "id": db_person[0],  # Pass the ID from the people table
        "AnonymizedStudentID": student.anonymized_student_ID,
        "AnonymizedStudentNumber": student.anonymized_student_number,
        "sections": student.sections,
        "SchlAssociated": student.schl_associated,
        "birthdate": student.birthdate,
        "SourcedID": student.sourced_ID,
        "GradeLevels": student.grade_levels
    })
    
    return result.fetchone()

# Helper function to insert into `teachers` table
def insert_teacher(db, teacher: PeopleInDBCreate, db_person):
    insert_teacher_query = text("""
        INSERT INTO teachers (id, anonymized_teacher_ID, anonymized_teacher_number, sections, stu_associated, schl_associated, site_duties,
                              credentials, subjects, siteduties, grade_levels, bd_demo)
        VALUES (:id, :anonymized_teacher_ID, :anonymized_teacher_number, :sections, :stu_associated, :schl_associated, :site_duties,
                :credentials, :subjects, :siteduties, :grade_levels, :bd_demo)
        RETURNING id, anonymized_teacher_ID, anonymized_teacher_number, sections, stu_associated, schl_associated, site_duties,
                  credentials, subjects, siteduties, grade_levels, bd_demo
    """)
    
    result = db.execute(insert_teacher_query, {
        "id": db_person[0],  # Use the id from the people table
        "anonymized_teacher_ID": teacher.anonymized_teacher_ID,
        "anonymized_teacher_number": teacher.anonymized_teacher_number,
        "sections": teacher.sections,
        "stu_associated": teacher.stu_associated,
        "schlassociated": teacher.schl_associated,
        "site_duties": teacher.site_duties,
        "credentials": teacher.credentials,
        "subjects": teacher.subjects,
        "siteduties": teacher.site_duties,
        "GradeLevels": teacher.grade_levels,
        "bd_demo": teacher.bd_demo
    })
    
    return result.fetchone()


@router.post("/people/", response_model=PeopleInDBResponse)
def create_person(person: PeopleInDBCreate, db: Session = Depends(get_db)):
    try:
        with db.begin():  # Ensuring atomic transactions
            # Insert into `people` table
            db_person = insert_person(db, person)
            
            if not db_person:
                raise HTTPException(status_code=500, detail="Failed to create person.")
            
            # Depending on role, insert into `students` or `teachers`
            student_data = None
            teacher_data = None
            
            if person.role == "student":
                db_student = insert_student(db, person, db_person)
                if not db_student:
                    raise HTTPException(status_code=500, detail="Failed to create student.")
                
                student_data = StudentInDBResponse(
                    id=db_student[0],
                    anonymizedstudentid=db_student[1],
                    anonymizedstudentnumber=db_student[2],
                    sections=db_student[3],
                    schlassociated=db_student[4],
                    birthdate=db_student[5]
                )
            
            elif person.role == "teacher":
                db_teacher = insert_teacher(db, person, db_person)
                if not db_teacher:
                    raise HTTPException(status_code=500, detail="Failed to create teacher.")
                
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
            
            # Construct response object
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

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from models.models import PeopleInDB
from schemas.schemas import PeopleInDBCreate, PeopleInDBResponse, TeacherInDBResponse, StudentInDBResponse
from databases.databases import get_db  # Ensure relative import is correct

router = APIRouter()

@router.post("/people/", response_model=PeopleInDBResponse)
def create_person(person: PeopleInDBCreate, db: Session = Depends(get_db)):
    try:
        db_person = PeopleInDB(
            firstname=person.firstname,
            lastname=person.Lastname,
            role=person.role,
            sourcedid=person.sourcedid,
            EnabledUser=person.EnabledUser,
            dateLastModified=person.DateLastModified,
            school_code=person.school_code
        )
        db.add(db_person)
        db.commit()
        db.refresh(db_person)

        # Insert the corresponding StudentInDB or TeacherInDB record based on the role
        if person.role == "student":
            query = text("""
                INSERT INTO students (id, AnonymizedStudentID, AnonymizedStudentNumber, Sections, SchlAssociated, Birthdate)
                VALUES (:id, :AnonymizedStudentID, :AnonymizedStudentNumber, :Sections, :SchlAssociated, :Birthdate)
                RETURNING id, AnonymizedStudentID, AnonymizedStudentNumber, Sections, SchlAssociated, Birthdate
            """)
            result = db.execute(query, {
                "id": db_person.id,
                "AnonymizedStudentID": person.AnonymizedStudentID,
                "AnonymizedStudentNumber": person.AnonymizedStudentNumber,
                "Sections": person.Sections,
                "SchlAssociated": person.SchlAssociated,
                "Birthdate": person.Birthdate
            })
            new_student = result.fetchone()

            if not new_student:
                raise HTTPException(status_code=500, detail="Failed to create student.")

            student_data = StudentInDBResponse(
                id=new_student[0],
                AnonymizedStudentID=new_student[1],
                AnonymizedStudentNumber=new_student[2],
                Sections=new_student[3],
                SchlAssociated=new_student[4],
                Birthdate=new_student[5]
            )
        elif person.role == "teacher":
            query = text("""
                INSERT INTO teachers (id, AnonymizedTeacherID, AnonymizedTeacherNumber, Sections, StuAssociated, SchlAssociated,
                                      Credentials, Subjects, SiteDuties, GradeLevels, BDDemo)
                VALUES (:id, :AnonymizedTeacherID, :AnonymizedTeacherNumber, :Sections, :StuAssociated, :SchlAssociated,
                        :Credentials, :Subjects, :SiteDuties, :GradeLevels, :BDdemo)
                RETURNING id, AnonymizedTeacherID, AnonymizedTeacherNumber, Sections, StuAssociated, SchlAssociated,
                          Credentials, Subjects, SiteDuties, GradeLevels, BDDemo
            """)
            result = db.execute(query, {
                "id": db_person.id,
                "AnonymizedTeacherID": person.AnonymizedTeacherID,
                "AnonymizedTeacherNumber": person.AnonymizedTeacherNumber,
                "Sections": person.Sections,
                "StuAssociated": person.StuAssociated,
                "SchlAssociated": person.SchlAssociated,
                "Credentials": person.Credentials,
                "Subjects": person.Subjects,
                "SiteDuties": person.SiteDuties,
                "GradeLevels": person.GradeLevels,
                "BDdemo": person.BDDemo if person.BDDemo else None
            })
            new_teacher = result.fetchone()

            if not new_teacher:
                raise HTTPException(status_code=500, detail="Failed to create teacher.")

            teacher_data = TeacherInDBResponse(
                id=new_teacher[0],
                AnonymizedTeacherID=new_teacher[1],
                AnonymizedTeacherNumber=new_teacher[2],
                Sections=new_teacher[3],
                StuAssociated=new_teacher[4],
                SchlAssociated=new_teacher[5],
                Credentials=new_teacher[6],
                Subjects=new_teacher[7],
                SiteDuties=new_teacher[8],
                GradeLevels=new_teacher[9],
                BDDemo=new_teacher[10]
            )

        # Commit the transaction
        db.commit()

        # Construct the response data
        response_person = PeopleInDBResponse(
            id=db_person.id,
            firstname=db_person.firstname,
            lastname=db_person.lastname,
            role=db_person.role,
            sourcedid=db_person.sourcedid,
            EnabledUser=db_person.EnabledUser,
            DateLastModified=db_person.dateLastModified,
            school_code=db_person.school_code,
            student=student_data if person.role == "student" else None,
            teacher=teacher_data if person.role == "teacher" else None
            #test

        )

        return response_person
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

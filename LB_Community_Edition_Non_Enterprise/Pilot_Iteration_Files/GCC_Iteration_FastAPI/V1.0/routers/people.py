from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from models.models import PeopleInDB, TeacherInDB, StudentInDB, RoleEnum
from schemas.schemas import PeopleInDBCreate, PeopleInDBResponse, TeacherInDBResponse, StudentInDBResponse
from databases.databases import get_db  # Ensure relative import is correct

router = APIRouter()

@router.post("/people", response_model=PeopleInDBResponse)
def create_person(person: PeopleInDBCreate, db: Session = Depends(get_db)):
    try:
        # Insert the person record
        query = text("""
            INSERT INTO people (Firstname, Lastname, role, sourcedid, EnabledUser, DateLastModified, school_code)
            VALUES (:Firstname, :Lastname, :role, :sourcedid, :EnabledUser, :DateLastModified, :school_code)
            RETURNING id, Firstname, Lastname, role, sourcedid, EnabledUser, DateLastModified, school_code
        """)
        result = db.execute(query, {
            "Firstname": person.Firstname,
            "Lastname": person.Lastname,
            "role": person.role.value,  # Ensure role is serialized correctly if it's an enum
            "sourcedid": person.sourcedid,
            "EnabledUser": person.EnabledUser,
            "DateLastModified": person.DateLastModified,
            "school_code": person.school_code
        })
        new_person = result.fetchone()

        if not new_person:
            raise HTTPException(status_code=500, detail="Failed to create person.")

        # Insert the corresponding StudentInDB or TeacherInDB record based on the role
        if person.role == RoleEnum.student:
            query = text("""
                INSERT INTO students (id, AnonymizedStudentID, AnonymizedStudentNumber, Sections, SchlAssociated, Birthdate)
                VALUES (:id, :AnonymizedStudentID, :AnonymizedStudentNumber, :Sections, :SchlAssociated, :Birthdate)
                RETURNING id, AnonymizedStudentID, AnonymizedStudentNumber, Sections, SchlAssociated, Birthdate
            """)
            result = db.execute(query, {
                "id": new_person["id"],
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
                id=new_student["id"],
                AnonymizedStudentID=new_student["AnonymizedStudentID"],
                AnonymizedStudentNumber=new_student["AnonymizedStudentNumber"],
                Sections=new_student["Sections"],
                SchlAssociated=new_student["SchlAssociated"],
                Birthdate=new_student["Birthdate"]
            )
        elif person.role == RoleEnum.teacher:
            query = text("""
                INSERT INTO teachers (id, AnonymizedTeacherID, AnonymizedTeacherNumber, Sections, StuAssociated, SchlAssociated,
                                      Credentials, Subjects, SiteDuties, GradeLevels, BDDemo)
                VALUES (:id, :AnonymizedTeacherID, :AnonymizedTeacherNumber, :Sections, :StuAssociated, :SchlAssociated,
                        :Credentials, :Subjects, :SiteDuties, :GradeLevels, :BDdemo)
                RETURNING id, AnonymizedTeacherID, AnonymizedTeacherNumber, Sections, StuAssociated, SchlAssociated,
                          Credentials, Subjects, SiteDuties, GradeLevels, BDDemo
            """)
            result = db.execute(query, {
                "id": new_person["id"],
                "AnonymizedTeacherID": person.AnonymizedTeacherID,
                "AnonymizedTeacherNumber": person.AnonymizedTeacherNumber,
                "Sections": person.Sections,
                "StuAssociated": person.StuAssociated,
                "SchlAssociated": person.SchlAssociated,
                "Credentials": person.Credentials,
                "Subjects": person.Subjects,
                "SiteDuties": person.SiteDuties,
                "GradeLevels": person.GradeLevels,
                "BDdemo": person.BDDemo.json() if person.BDDemo else None
            })
            new_teacher = result.fetchone()

            if not new_teacher:
                raise HTTPException(status_code=500, detail="Failed to create teacher.")

            teacher_data = TeacherInDBResponse(
                id=new_teacher["id"],
                AnonymizedTeacherID=new_teacher["AnonymizedTeacherID"],
                AnonymizedTeacherNumber=new_teacher["AnonymizedTeacherNumber"],
                Sections=new_teacher["Sections"],
                StuAssociated=new_teacher["StuAssociated"],
                SchlAssociated=new_teacher["SchlAssociated"],
                Credentials=new_teacher["Credentials"],
                Subjects=new_teacher["Subjects"],
                SiteDuties=new_teacher["SiteDuties"],
                GradeLevels=new_teacher["GradeLevels"],
                BDDemo=new_teacher["BDDemo"]
            )

        # Commit the transaction
        db.commit()

        # Construct the response data
        response_person = PeopleInDBResponse(
            id=new_person["id"],
            Firstname=new_person["Firstname"],
            Lastname=new_person["Lastname"],
            role=new_person["role"],
            sourcedid=new_person["sourcedid"],
            EnabledUser=new_person["EnabledUser"],
            DateLastModified=new_person["DateLastModified"],
            school_code=new_person["school_code"],
            student=student_data if person.role == RoleEnum.student else None,
            teacher=teacher_data if person.role == RoleEnum.teacher else None
        )

        return response_person
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from models.models import PeopleInDB, TeacherInDB, RoleEnum
from schemas.schemas import (
    PeopleInDBUpdate, PeopleInDBResponse, 
    TeacherInDBResponse, StudentInDBResponse, 
    StudentInDB, BDDemoModel, PeopleInDBCreate
)
from databases.databases import get_db  # Use relative import

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
            "role": person.role,
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

@router.put("/people/{person_id}", response_model=PeopleInDBResponse)
def update_person(person_id: int, person: PeopleInDBUpdate, db: Session = Depends(get_db)):
    try:
        # Find the person in the PeopleInDB table
        db_person = db.query(PeopleInDB).filter(PeopleInDB.id == person_id).first()
        
        if db_person is None:
            raise HTTPException(status_code=404, detail="Person not found")

        # Update the person record
        query = text("""
            UPDATE people
            SET Firstname = :Firstname, Lastname = :Lastname, sourcedid = :sourcedid, 
                EnabledUser = :EnabledUser, DateLastModified = :DateLastModified, school_code = :school_code
            WHERE id = :person_id
            RETURNING id, Firstname, Lastname, role, sourcedid, EnabledUser, DateLastModified, school_code
        """)
        result = db.execute(query, {
            "Firstname": person.Firstname,
            "Lastname": person.Lastname,
            "sourcedid": person.sourcedid,
            "EnabledUser": person.EnabledUser,
            "DateLastModified": person.DateLastModified,
            "school_code": person.school_code,
            "person_id": person_id
        })
        updated_person = result.fetchone()

        if not updated_person:
            raise HTTPException(status_code=500, detail="Failed to update person.")

        # Update the corresponding StudentInDB or TeacherInDB record based on the role
        if db_person.role == RoleEnum.student:
            query = text("""
                UPDATE students
                SET AnonymizedStudentID = :AnonymizedStudentID, AnonymizedStudentNumber = :AnonymizedStudentNumber,
                    Sections = :Sections, SchlAssociated = :SchlAssociated, Birthdate = :Birthdate
                WHERE id = :person_id
                RETURNING id, AnonymizedStudentID, AnonymizedStudentNumber, Sections, SchlAssociated, Birthdate
            """)
            result = db.execute(query, {
                "AnonymizedStudentID": person.AnonymizedStudentID,
                "AnonymizedStudentNumber": person.AnonymizedStudentNumber,
                "Sections": person.Sections,
                "SchlAssociated": person.SchlAssociated,
                "Birthdate": person.Birthdate,
                "person_id": person_id
            })
            updated_student = result.fetchone()

            if not updated_student:
                raise HTTPException(status_code=500, detail="Failed to update student.")

            student_data = StudentInDBResponse(
                id=updated_student["id"],
                AnonymizedStudentID=updated_student["AnonymizedStudentID"],
                AnonymizedStudentNumber=updated_student["AnonymizedStudentNumber"],
                Sections=updated_student["Sections"],
                SchlAssociated=updated_student["SchlAssociated"],
                Birthdate=updated_student["Birthdate"]
            )
        elif db_person.role == RoleEnum.teacher:
            query = text("""
                UPDATE teachers
                SET AnonymizedTeacherID = :AnonymizedTeacherID, AnonymizedTeacherNumber = :AnonymizedTeacherNumber,
                    Sections = :Sections, StuAssociated = :StuAssociated, SchlAssociated = :SchlAssociated,
                    Credentials = :Credentials, Subjects = :Subjects, SiteDuties = :SiteDuties,
                    GradeLevels = :GradeLevels, BDDemo = :BDdemo
                WHERE id = :person_id
                RETURNING id, AnonymizedTeacherID, AnonymizedTeacherID, Sections, StuAssociated, SchlAssociated,
                          Credentials, Subjects, SiteDuties, GradeLevels, BDDemo
            """)
            result = db.execute(query, {
                "AnonymizedTeacherID": person.AnonymizedTeacherID,
                "AnonymizedTeacherNumber": person.AnonymizedTeacherNumber,
                "Sections": person.Sections,
                "StuAssociated": person.StuAssociated,
                "SchlAssociated": person.SchlAssociated,
                "Credentials": person.Credentials,
                "Subjects": person.Subjects,
                "SiteDuties": person.SiteDuties,
                "GradeLevels": person.GradeLevels,
                "BDdemo": person.BDDemo.json() if person.BDDemo else None,
                "person_id": person_id
            })
            updated_teacher = result.fetchone()

            if not updated_teacher:
                raise HTTPException(status_code=500, detail="Failed to update teacher.")

            teacher_data = TeacherInDBResponse(
                id=updated_teacher["id"],
                AnonymizedTeacherID=updated_teacher["AnonymizedTeacherID"],
                AnonymizedTeacherNumber=updated_teacher["AnonymizedTeacherNumber"],
                Sections=updated_teacher["Sections"],
                StuAssociated=updated_teacher["StuAssociated"],
                SchlAssociated=updated_teacher["SchlAssociated"],
                Credentials=updated_teacher["Credentials"],
                Subjects=updated_teacher["Subjects"],
                SiteDuties=updated_teacher["SiteDuties"],
                GradeLevels=updated_teacher["GradeLevels"],
                BDDemo=updated_teacher["BDDemo"]
            )

        # Commit the transaction
        db.commit()

        # Construct the response data
        response_person = PeopleInDBResponse(
            id=updated_person["id"],
            Firstname=updated_person["Firstname"],
            Lastname=updated_person["Lastname"],
            role=updated_person["role"],
            sourcedid=updated_person["sourcedid"],
            EnabledUser=updated_person["EnabledUser"],
            DateLastModified=updated_person["DateLastModified"],
            school_code=updated_person["school_code"],
            student=student_data if db_person.role == RoleEnum.student else None,
            teacher=teacher_data if db_person.role == RoleEnum.teacher else None
        )

        return response_person
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/people/{person_id}", response_model=PeopleInDBResponse)
def get_person(person_id: int, db: Session = Depends(get_db)):
    try:
        # Find the person in the PeopleInDB table
        db_person = db.query(PeopleInDB).filter(PeopleInDB.id == person_id).first()
        
        if db_person is None:
            raise HTTPException(status_code=404, detail="Person not found")

        # Construct the base response for the person
        response_person = PeopleInDBResponse(
            id=db_person.id,
            Firstname=db_person.Firstname,
            Lastname=db_person.Lastname,
            role=db_person.role,
            sourcedid=db_person.sourcedid,
            EnabledUser=db_person.EnabledUser,
            DateLastModified=db_person.DateLastModified,
            school_code=db_person.school_code
        )

        # Fetch additional data based on the role
        if db_person.role == RoleEnum.student:
            student = db.query(StudentInDB).filter(StudentInDB.id == person_id).first()
            if student is None:
                raise HTTPException(status_code=404, detail="Student details not found")

            response_person.student = StudentInDBResponse(
                id=student.id,
                AnonymizedStudentID=student.AnonymizedStudentID,
                AnonymizedStudentNumber=student.AnonymizedStudentNumber,
                Sections=student.Sections,
                SchlAssociated=student.SchlAssociated,
                Birthdate=student.Birthdate
            )
        elif db_person.role == RoleEnum.teacher:
            teacher = db.query(TeacherInDB).filter(TeacherInDB.id == person_id).first()
            if teacher is None:
                raise HTTPException(status_code=404, detail="Teacher details not found")

            response_person.teacher = TeacherInDBResponse(
                id=teacher.id,
                AnonymizedTeacherID=teacher.AnonymizedTeacherID,
                AnonymizedTeacherNumber=teacher.AnonymizedTeacherNumber,
                Sections=teacher.Sections,
                StuAssociated=teacher.StuAssociated,
                SchlAssociated=teacher.SchlAssociated,
                Credentials=teacher.Credentials,
                Subjects=teacher.Subjects,
                SiteDuties=teacher.SiteDuties,
                GradeLevels=teacher.GradeLevels,
                BDDemo=teacher.BDDemo
            )

        return response_person
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
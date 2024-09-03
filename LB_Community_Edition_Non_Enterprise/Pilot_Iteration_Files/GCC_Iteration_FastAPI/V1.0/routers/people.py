from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from models.models import PeopleInDB, RoleEnum
from schemas.schemas import (
    PeopleInDBCreate, PeopleInDBResponse, 
    StudentInDBResponse, TeacherInDBResponse,
    BDDemoModel
)
from databases.databases import get_db  # Use relative import

router = APIRouter()

@router.post("/people/", response_model=PeopleInDBResponse)
def create_person(person: PeopleInDBCreate, db: Session = Depends(get_db)):
    try:
        # Insert the PeopleInDB record using raw SQL and return the inserted record
        query = text("""
            INSERT INTO people (Firstname, Lastname, role, sourcedid, EnabledUser, DateLastModified, school_code)
            VALUES (:Firstname, :Lastname, :role, :sourcedid, :EnabledUser, :DateLastModified, :school_code)
            RETURNING id, Firstname, Lastname, role, sourcedid, EnabledUser, DateLastModified, school_code
        """)
        result = db.execute(query, {
            "Firstname": person.Firstname,
            "Lastname": person.Lastname,
            "role": person.role.value,
            "sourcedid": person.sourcedid,
            "EnabledUser": person.EnabledUser,
            "DateLastModified": person.DateLastModified,
            "school_code": person.school_code
        })
        db_person = result.fetchone()

        if not db_person:
            raise HTTPException(status_code=500, detail="Failed to create person.")

        db_student = None
        db_teacher = None

        # Insert the corresponding StudentInDB or TeacherInDB record based on the role
        if person.role == RoleEnum.student:
            query = text("""
                INSERT INTO students (AnonymizedStudentID, AnonymizedStudentNumber, role, sourcedid)
                VALUES (:AnonymizedStudentID, :AnonymizedStudentNumber, :role, :sourcedid)
                RETURNING id, AnonymizedStudentID, AnonymizedStudentNumber, role, sourcedid
            """)
            result = db.execute(query, {
                "AnonymizedStudentID": person.AnonymizedStudentID,
                "AnonymizedStudentNumber": person.AnonymizedStudentNumber,
                "role": person.role.value,
                "sourcedid": person.sourcedid
            })
            db_student = result.fetchone()

            if not db_student:
                raise HTTPException(status_code=500, detail="Failed to create student.")

        elif person.role == RoleEnum.teacher:
            query = text("""
                INSERT INTO teachers (AnonymizedTeacherID, AnonymizedTeacherNumber, role, sourcedid, sections, stu_associated, schl_associated, credentials, subjects, site_duties, grade_levels)
                VALUES (:AnonymizedTeacherID, :AnonymizedTeacherNumber, :role, :sourcedid, :sections, :stu_associated, :schl_associated, :credentials, :subjects, :site_duties, :grade_levels)
                RETURNING id, AnonymizedTeacherID, AnonymizedTeacherNumber, role, sourcedid
            """)
            result = db.execute(query, {
                "AnonymizedTeacherID": person.AnonymizedTeacherID,
                "AnonymizedTeacherNumber": person.AnonymizedTeacherNumber,
                "role": person.role.value,
                "sourcedid": person.sourcedid,
                "sections": person.sections,
                "stu_associated": person.stu_associated,
                "schl_associated": person.schl_associated,
                "credentials": person.credentials,
                "subjects": person.subjects,
                "site_duties": person.site_duties,
                "grade_levels": person.grade_levels
            })
            db_teacher = result.fetchone()

            if not db_teacher:
                raise HTTPException(status_code=500, detail="Failed to create teacher.")

        # Commit the transaction
        db.commit()

        # Construct the response data
        response_person = PeopleInDBResponse(
            id=db_person["id"],
            Firstname=db_person["Firstname"],
            Lastname=db_person["Lastname"],
            role=db_person["role"],
            sourcedid=db_person["sourcedid"],
            EnabledUser=db_person["EnabledUser"],
            DateLastModified=db_person["DateLastModified"],
            school_code=db_person["school_code"],
            student=db_student if person.role == RoleEnum.student else None,
            teacher=db_teacher if person.role == RoleEnum.teacher else None
        )

        return response_person
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/people/{person_id}", response_model=PeopleInDBResponse)
def read_person(person_id: int, db: Session = Depends(get_db)):
    try:
        db_person = db.query(PeopleInDB).filter(PeopleInDB.id == person_id).first()
        if db_person is None:
            raise HTTPException(status_code=404, detail="Person not found")
        
        # Retrieve the associated student or teacher record based on the role
        db_student = None
        db_teacher = None
        
        if db_person.role == RoleEnum.student:
            db_student = db.query(StudentInDBResponse).filter_by(sourcedid=db_person.sourcedid).first()
        elif db_person.role == RoleEnum.teacher:
            db_teacher = db.query(TeacherInDBResponse).filter_by(sourcedid=db_person.sourcedid).first()

        response_person = PeopleInDBResponse(
            id=db_person.id,
            Firstname=db_person.Firstname,
            Lastname=db_person.Lastname,
            role=db_person.role,
            sourcedid=db_person.sourcedid,
            EnabledUser=db_person.EnabledUser,
            DateLastModified=db_person.DateLastModified,
            school_code=db_person.school_code,
            student=db_student,
            teacher=db_teacher
        )

        return response_person
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.put("/teachers/{teacher_id}/update_teacher_bddemo", response_model=TeacherInDBResponse, summary="Update Teacher BDDemo")
def update_bddemo(teacher_id: int, bddemo: BDDemoModel, db: Session = Depends(get_db)):
    try:
        # Find the teacher by ID
        db_teacher = db.query(TeacherInDBResponse).filter_by(id=teacher_id).first()

        if db_teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found")

        # Update the BDDemo column with new data using raw SQL
        query = text("""
            UPDATE teachers
            SET BDDemo = :bddemo
            WHERE id = :teacher_id
            RETURNING id, AnonymizedTeacherID, AnonymizedTeacherNumber, role, sourcedid, BDDemo
        """)
        result = db.execute(query, {
            "bddemo": bddemo.json(),  # Convert BDDemoModel to JSON string
            "teacher_id": teacher_id
        })
        updated_teacher = result.fetchone()

        if not updated_teacher:
            raise HTTPException(status_code=500, detail="Failed to update BDDemo.")

        # Commit the transaction
        db.commit()

        # Construct the response data
        response_teacher = TeacherInDBResponse(
            id=updated_teacher["id"],
            AnonymizedTeacherID=updated_teacher["AnonymizedTeacherID"],
            AnonymizedTeacherNumber=updated_teacher["AnonymizedTeacherNumber"],
            role=updated_teacher["role"],
            sourcedid=updated_teacher["sourcedid"],
            BDDemo=bddemo
        )

        return response_teacher
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

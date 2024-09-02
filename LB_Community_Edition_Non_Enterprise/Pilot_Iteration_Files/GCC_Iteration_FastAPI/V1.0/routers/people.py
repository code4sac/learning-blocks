from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.models import PeopleInDB 
from schemas.schemas import PeopleInDBCreate, PeopleInDBResponse
from databases.databases import get_db  # Use relative import
from models.models import RoleEnum
from sqlalchemy import text

router = APIRouter()
router = APIRouter()

@router.post("/people/", response_model=PeopleInDBResponse)
def create_person(person: PeopleInDBCreate, db: Session = Depends(get_db)):
    try:
        # Create the PeopleInDB record using raw SQL
        query = text("""
            INSERT INTO people (name, age, role, sourcedid, school_code)
            VALUES (:name, :age, :role, :sourcedid, :school_code)
            RETURNING id, name, age, role, sourcedid, school_code
        """)
        result = db.execute(query, {
            "name": person.name,
            "age": person.age,
            "role": person.role,
            "sourcedid": person.sourcedid,
            "school_code": person.school_code
        })
        db_person = result.fetchone()

        if not db_person:
            raise HTTPException(status_code=500, detail="Failed to create person.")

        # Based on the role, create the corresponding StudentInDB or TeacherInDB record
        if person.role == RoleEnum.student:
            query = text("""
                INSERT INTO students (AnonymizedStudentID, AnonymizedStudentNumber, role, sourcedid)
                VALUES (:AnonymizedStudentID, :AnonymizedStudentNumber, :role, :sourcedid)
                RETURNING id, AnonymizedStudentID, AnonymizedStudentNumber, role, sourcedid
            """)
            result = db.execute(query, {
                "AnonymizedStudentID": person.AnonymizedStudentID,
                "AnonymizedStudentNumber": person.AnonymizedStudentNumber,
                "role": person.role,
                "sourcedid": person.sourcedid
            })
            db_student = result.fetchone()

            if not db_student:
                raise HTTPException(status_code=500, detail="Failed to create student.")
        
        elif person.role == RoleEnum.teacher:
            query = text("""
                INSERT INTO teachers (AnonymizedTeacherID, AnonymizedTeacherNumber, role, sourcedid)
                VALUES (:AnonymizedTeacherID, :AnonymizedTeacherNumber, :role, :sourcedid)
                RETURNING id, AnonymizedTeacherID, AnonymizedTeacherNumber, role, sourcedid
            """)
            result = db.execute(query, {
                "AnonymizedTeacherID": person.AnonymizedStudentID,  # Adjust as needed
                "AnonymizedTeacherNumber": person.AnonymizedStudentNumber,
                "role": person.role,
                "sourcedid": person.sourcedid
            })
            db_teacher = result.fetchone()

            if not db_teacher:
                raise HTTPException(status_code=500, detail="Failed to create teacher.")

        # Return the created person along with the related student/teacher record
        response_person = {
            "id": db_person["id"],
            "name": db_person["name"],
            "age": db_person["age"],
            "role": db_person["role"],
            "sourcedid": db_person["sourcedid"],
            "school_code": db_person["school_code"],
            "student": db_student if person.role == RoleEnum.student else None,
            "teacher": db_teacher if person.role == RoleEnum.teacher else None
        }
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
        return db_person
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

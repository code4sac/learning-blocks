from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.models import StudentInDB, PeopleInDB
from schemas.schemas import StudentInDBCreate, StudentInDBResponse
from databases.databases import get_db  # Use relative import

router = APIRouter()

@router.post("/students/", response_model=StudentInDBResponse)
def create_student(student: StudentInDBCreate, db: Session = Depends(get_db)):
    # Check if the associated PeopleInDB record exists using anonymizedStudentID
    person = db.query(PeopleInDB).filter(PeopleInDB.AnonymizedStudentID == student.anonymizedStudentID).first()
    if not person:
        raise HTTPException(status_code=404, detail="Associated person not found")

    # Create and add the new student record
    new_student = StudentInDB(
        anonymizedStudentID=student.anonymizedStudentID,
        anonymizedStudentNumber=student.anonymizedStudentNumber,
        role=student.role,
        people=person
    )

    try:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error occurred")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

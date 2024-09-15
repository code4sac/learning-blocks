import json
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from models.models import StudentInDB
from schemas.schemas import StudentInDBCreate, StudentInDBResponse, BDDemoModel
from databases.databases import get_db  # Ensure relative import is correct

router = APIRouter()

@router.post("/student", response_model=StudentInDBResponse)
def create_school(student: StudentInDBCreate, db: Session = Depends(get_db)):
        # Deserialize MetaData from JSON string

    try:
        
        db_student = StudentInDB(
            FirstName=student.FirstName,
            LastName=student.LastName,
            SchoolCode=student.SchoolCode,
            AnonymizedStudentID=student.AnonymizedStudentID,
            AnonymizedStudentNumber=student.AnonymizedStudentNumber,
            Role=student.Role,
            SourcedID=student.SourcedID,
            Sections=student.Sections,
            SchlAssociated=student.SchlAssociated,
            Birthdate=student.Birthdate,
            GradeLevels=student.GradeLevels,
            MetaData=json.dumps(student.MetaData.dict()) if student.MetaData else None
            
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)

        return db_student
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    
@router.get("/students/{student_id}", response_model=StudentInDBResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    try:
        db_student = db.query(StudentInDB).filter(StudentInDB.id == student_id).first()
        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        response_student = StudentInDBResponse(
            id=db_student.id,
            AnonymizedStudentID=db_student.AnonymizedStudentID,
            AnonymizedStudentNumber=db_student.AnonymizedStudentNumber,
            role=db_student.Role,
            sourcedid=db_student.SourcedID,
            SchoolCode=db_student.SchoolCode,
            MetaData=db_student.MetaData
        )
        
        return response_student
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


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
            MetaData=json.dumps(student.MetaData.dict()) if student.MetaData else None,
            EnabledUser=student.EnabledUser,
            DateLastModified=student.DateLastModified ,
            StuAssociated=student.StuAssociated
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
        db_student = db.query(StudentInDB).filter(StudentInDB.ID == student_id).first()
        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        # Ensure MetaData is a valid JSON string or None
        try:
            meta_data = json.loads(db_student.MetaData) if db_student.MetaData else None
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="MetaData is not a valid JSON string")
        
        # Create the response object with the appropriate fields
        response_student = StudentInDBResponse(
            ID=db_student.ID,
            FirstName=db_student.FirstName,
            LastName=db_student.LastName,
            SchoolCode=db_student.SchoolCode,
            AnonymizedStudentID=db_student.AnonymizedStudentID,
            AnonymizedStudentNumber=db_student.AnonymizedStudentNumber,
            Role=db_student.Role,
            SourcedID=db_student.SourcedID,
            Sections=db_student.Sections,
            SchlAssociated=db_student.SchlAssociated,
            Birthdate=db_student.Birthdate,
            GradeLevels=db_student.GradeLevels,
            MetaData=meta_data,  # Ensure MetaData is a valid dictionary
            EnabledUser=db_student.EnabledUser,
            DateLastModified=db_student.DateLastModified,
            StuAssociated=db_student.StuAssociated
        )
        
        return response_student
    except HTTPException as e:
        raise e  # Forward the HTTP exception as is
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

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

    
import json

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
        
        # Convert stringified lists to actual lists
        sections = json.loads(db_student.Sections) if isinstance(db_student.Sections, str) else db_student.Sections
        stu_associated = json.loads(db_student.StuAssociated) if isinstance(db_student.StuAssociated, str) else db_student.StuAssociated
        grade_levels = json.loads(db_student.GradeLevels) if isinstance(db_student.GradeLevels, str) else db_student.GradeLevels
        
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
            Sections=sections,  # Ensure it's a valid list
            SchlAssociated=db_student.SchlAssociated,
            Birthdate=db_student.Birthdate,
            GradeLevels=grade_levels,  # Ensure it's a valid list
            MetaData=meta_data,  # Ensure MetaData is a valid dictionary
            EnabledUser=db_student.EnabledUser,
            DateLastModified=db_student.DateLastModified,
            StuAssociated=stu_associated  # Ensure it's a valid list
        )
        
        return response_student
    except HTTPException as e:
        raise e  # Forward the HTTP exception as is
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

from typing import List
import json
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from models.models import StudentInDB
from schemas.schemas import StudentInDBCreate, StudentInDBResponse, BDDemoModel
from databases.databases import get_db  # Ensure relative import is correct

router = APIRouter()

@router.post("/student", response_model=StudentInDBResponse, description="Add a new student.",
            summary="Add a new student.",
            response_description="Add a new student.")
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


@router.get("/students", response_model=List[StudentInDBResponse], description="Retrieve all students",
            summary="Retrieve all students",
            response_description="Retrieve all students")
def read_students(db: Session = Depends(get_db)):
    try:
        db_students = db.query(StudentInDB).all()
        response_students = []

        for db_student in db_students:
            # Ensure MetaData is a valid JSON string or None
            try:
                meta_data = json.loads(db_student.MetaData) if db_student.MetaData else None
            except json.JSONDecodeError:
                raise HTTPException(status_code=500, detail="MetaData is not a valid JSON string")

            # Convert Sections if it's a string
            if isinstance(db_student.Sections, str):
                try:
                    sections = json.loads(db_student.Sections)
                except json.JSONDecodeError:
                    # Fallback if Sections is not valid JSON, assuming it's a comma-separated string
                    sections = db_student.Sections.split(",") if db_student.Sections else []
            else:
                sections = db_student.Sections if db_student.Sections else []

            # Convert StuAssociated if it's a string
            if isinstance(db_student.StuAssociated, str):
                try:
                    stu_associated = json.loads(db_student.StuAssociated)
                except json.JSONDecodeError:
                    stu_associated = db_student.StuAssociated.split(",") if db_student.StuAssociated else []
            else:
                stu_associated = db_student.StuAssociated if db_student.StuAssociated else []

            
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
                Sections=sections,  # Should now be a list
                SchlAssociated=db_student.SchlAssociated,
                Birthdate=db_student.Birthdate,
                EnabledUser=db_student.EnabledUser,
                GradeLevels=db_student.GradeLevels,  # Should now be a list
                MetaData=meta_data,  # Should be a dictionary
                DateLastModified=db_student.DateLastModified,
                StuAssociated=stu_associated  # Should now be a list
            )
            
            response_students.append(response_student)

        return response_students
    except HTTPException as e:
        raise e  # Forward the HTTP exception as is
    except Exception as e:
        # Add more details to the error message for debugging
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
    from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional
import json

@router.get("/students/{anonymized_student_id}", response_model=StudentInDBResponse,description="Retrieve a student's information using their AnonymizedStudentID.",
            summary="Get student by AnonymizedStudentID",
            response_description="The student details for the given AnonymizedStudentID.")
def read_student(anonymized_student_id: str, db: Session = Depends(get_db)):
    try:
        # Query for a single student based on AnonymizedStudentID
        db_student = db.query(StudentInDB).filter(StudentInDB.AnonymizedStudentID == anonymized_student_id).first()
        
        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")

        # Ensure MetaData is a valid JSON string or None
        try:
            meta_data = json.loads(db_student.MetaData) if db_student.MetaData else None
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="MetaData is not a valid JSON string")

        # Convert Sections if it's a string
        if isinstance(db_student.Sections, str):
            try:
                sections = json.loads(db_student.Sections)
            except json.JSONDecodeError:
                sections = db_student.Sections.split(",") if db_student.Sections else []
        else:
            sections = db_student.Sections if db_student.Sections else []

        # Convert StuAssociated if it's a string
        if isinstance(db_student.StuAssociated, str):
            try:
                stu_associated = json.loads(db_student.StuAssociated)
            except json.JSONDecodeError:
                stu_associated = db_student.StuAssociated.split(",") if db_student.StuAssociated else []
        else:
            stu_associated = db_student.StuAssociated if db_student.StuAssociated else []


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
            Sections=sections,  # Should now be a list
            SchlAssociated=db_student.SchlAssociated,
            Birthdate=db_student.Birthdate,
            EnabledUser=db_student.EnabledUser,
            GradeLevels=db_student.GradeLevels,  # Should now be a list
            MetaData=meta_data,  # Should be a dictionary
            DateLastModified=db_student.DateLastModified,
            StuAssociated=stu_associated  # Should now be a list
        )
        
        return response_student
    except HTTPException as e:
        raise e  # Forward the HTTP exception as is
    except Exception as e:
        # Add more details to the error message for debugging
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

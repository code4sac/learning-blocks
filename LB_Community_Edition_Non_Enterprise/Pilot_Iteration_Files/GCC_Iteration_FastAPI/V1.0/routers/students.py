from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from models.models import StudentInDB
from schemas.schemas import (
    StudentInDBCreate, StudentInDBResponse, 
    BDDemoModel
)
from databases.databases import get_db  # Use relative import

router = APIRouter()

@router.post("/students/", response_model=StudentInDBResponse)
def create_student(student: StudentInDBCreate, db: Session = Depends(get_db)):
    try:
        # Insert the StudentInDB record using raw SQL and return the inserted record
        query = text("""
            INSERT INTO students (AnonymizedStudentID, AnonymizedStudentNumber, role, sourcedid, Sections, SchlAssociated, Birthdate, BDDemo)
            VALUES (:AnonymizedStudentID, :AnonymizedStudentNumber, :role, :sourcedid, :Sections, :SchlAssociated, :Birthdate, :BDDemoModel)
            RETURNING id, AnonymizedStudentID, AnonymizedStudentNumber, role, sourcedid, Sections, SchlAssociated, Birthdate, BDDemo
        """)
        result = db.execute(query, {
            "AnonymizedStudentID": student.AnonymizedStudentID,
            "AnonymizedStudentNumber": student.AnonymizedStudentNumber,
            "role": student.role.value,
            "sourcedid": student.sourcedid,
            "Sections": student.Sections,
            "SchlAssociated": student.SchlAssociated,
            "Birthdate": student.Birthdate,
            "BDDemoModel": student.BDDemoModel.model_dump_json()
    
        })
        db_student = result.fetchone()

        if not db_student:
            raise HTTPException(status_code=500, detail="Failed to create student.")

        # Commit the transaction
        db.commit()

        # Construct the response data
        response_student = StudentInDBResponse(
            id=db_student["id"],
            AnonymizedStudentID=db_student["AnonymizedStudentID"],
            AnonymizedStudentNumber=db_student["AnonymizedStudentNumber"],
            role=db_student["role"],
            sourcedid=db_student["sourcedid"]
        )

        return response_student
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
            role=db_student.role,
            sourcedid=db_student.sourcedid
        )

        return response_student
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.put("/students/{student_id}/update_student_bddemo", response_model=StudentInDBResponse, summary="Update Student BDDemo")
def update_bddemo(student_id: int, bddemo: BDDemoModel, db: Session = Depends(get_db)):
    try:
        # Find the student by ID
        db_student = db.query(StudentInDB).filter_by(id=student_id).first()

        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")

        # Update the BDDemo column with new data using raw SQL
        query = text("""
            UPDATE students
            SET BDDemo = :bddemo
            WHERE id = :student_id
            RETURNING id, AnonymizedStudentID, AnonymizedStudentNumber, role, sourcedid, BDDemo, Sections, SchlAssociated, Birthdate
        """)
        result = db.execute(query, {
            "bddemo": bddemo.model_dump_json(),  # Convert BDDemoModel to JSON string
            "student_id": student_id
        })
        updated_student = result.fetchone()

        if not updated_student:
            raise HTTPException(status_code=500, detail="Failed to update BDDemo.")

        # Commit the transaction
        db.commit()

        # Construct the response data
        response_student = StudentInDBResponse(
            id=updated_student["id"],
            AnonymizedStudentID=updated_student["AnonymizedStudentID"],
            AnonymizedStudentNumber=updated_student["AnonymizedStudentNumber"],
            role=updated_student["role"],
            sourcedid=updated_student["sourcedid"],
            BDDemo=bddemo
        )

        return response_student
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from models.models import PeopleInDB, RoleEnum, TeacherInDB
from schemas.schemas import (
    PeopleInDBCreate, PeopleInDBResponse, 
    TeacherInDBResponse, BDDemoModel
)
from databases.databases import get_db  # Use relative import

router = APIRouter()

@router.post("/teachers/", response_model=TeacherInDBResponse)
def create_teacher(teacher: TeacherInDBResponse, db: Session = Depends(get_db)):
    if teacher.role != RoleEnum.teacher:
        raise HTTPException(status_code=400, detail="Role must be teacher.")

    try:
        # Insert the PeopleInDB record for teacher
        query = text("""
            INSERT INTO people (Firstname, Lastname, role, sourcedid, EnabledUser, DateLastModified, school_code, grade_levels)
            VALUES (:Firstname, :Lastname, :role, :sourcedid, :EnabledUser, :DateLastModified, :school_code, :grade_levels)
            RETURNING id, Firstname, Lastname, role, sourcedid, EnabledUser, DateLastModified, school_code, grade_levels
        """)
        result = db.execute(query, {
            "anonymizedteacherid": teacher.AnonymizedTeacherID,
            "anonymizedteachernumber": teacher.AnonymizedTeacherNumber,
            "sections": teacher.Sections,
            "stu_associated": teacher.StuAssociated,
            "schl_associated": teacher.SchlAssociated,
            "credentials": teacher.Credentials,
            "subjects": teacher.Subjects,
            "role": teacher.role.value,
            "sourcedid": teacher.sourcedid,
            "EnabledUser": teacher.EnabledUser,
            "DateLastModified": teacher.DateLastModified,
            "school_code": teacher.school_code,
            "grade_levels": teacher.GradeLevels,
            "bddemo": teacher.bddemo.json() if teacher.bddemo else None
        })
        db_person = result.fetchone()

        if not db_person:
            raise HTTPException(status_code=500, detail="Failed to create person.")

        # Insert the TeacherInDB record
        query = text("""
            INSERT INTO teachers (id, AnonymizedTeacherID, AnonymizedTeacherNumber, sections, stu_associated, schl_associated, credentials, subjects, site_duties, grade_levels)
            VALUES (:id, :AnonymizedTeacherID, :AnonymizedTeacherNumber, :sections, :stu_associated, :schl_associated, :credentials, :subjects, :site_duties, :grade_levels)
            RETURNING id, AnonymizedTeacherID, AnonymizedTeacherNumber, sections, stu_associated, schl_associated, credentials, subjects, site_duties, grade_levels
        """)
        result = db.execute(query, {
            "id": db_person["id"],
            "AnonymizedTeacherID": teacher.AnonymizedTeacherID,
            "AnonymizedTeacherNumber": teacher.AnonymizedTeacherNumber,
            "sections": teacher.Sections,
            "stu_associated": teacher.StuAssociated,
            "schl_associated": teacher.SchlAssociated,
            "credentials": teacher.Credentials,
            "subjects": teacher.Subjects,
            "site_duties": teacher.SiteDuties,
            "grade_levels": teacher.GradeLevels,
            "role": teacher.role.value,
            "sourcedid": teacher.sourcedid,
            "EnabledUser": teacher.EnabledUser,
            "DateLastModified": teacher.DateLastModified,
            "school_code": teacher.school_code,
            "bddemo": teacher.bddemo.json() if teacher.bddemo else None
    
        })
        db_teacher = result.fetchone()

        if not db_teacher:
            raise HTTPException(status_code=500, detail="Failed to create teacher.")

        # Commit the transaction
        db.commit()

        # Construct the response data
        response_teacher = TeacherInDBResponse(
            id=db_teacher["id"],
            AnonymizedTeacherID=db_teacher["AnonymizedTeacherID"],
            AnonymizedTeacherNumber=db_teacher["AnonymizedTeacherNumber"],
            sections=db_teacher["sections"],
            stu_associated=db_teacher["stu_associated"],
            schl_associated=db_teacher["schl_associated"],
            credentials=db_teacher["credentials"],
            subjects=db_teacher["subjects"],
            site_duties=db_teacher["site_duties"],
            grade_levels=db_teacher["grade_levels"]
        )

        return response_teacher
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/teachers/{teacher_id}", response_model=TeacherInDBResponse)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    try:
        db_teacher = db.query(TeacherInDB).filter(TeacherInDB.id == teacher_id).first()
        if db_teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found")

        # Construct the response data
        response_teacher = TeacherInDBResponse(
            id=db_teacher.id,
            AnonymizedTeacherID=db_teacher.AnonymizedTeacherID,
            AnonymizedTeacherNumber=db_teacher.AnonymizedTeacherNumber,
            sections=db_teacher.Sections,
            stu_associated=db_teacher.StuAssociated,
            schl_associated=db_teacher.SchlAssociated,
            credentials=db_teacher.Credentials,
            subjects=db_teacher.Subjects,
            site_duties=db_teacher.SiteDuties,
            grade_levels=db_teacher.GradeLevels
        )

        return response_teacher
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.put("/teachers/{teacher_id}/update_teacher_bddemo", response_model=TeacherInDBResponse, summary="Update Teacher BDDemo")
def update_bddemo(teacher_id: int, bddemo: BDDemoModel, db: Session = Depends(get_db)):
    try:
        # Find the teacher by ID
        db_teacher = db.query(TeacherInDB).filter(TeacherInDB.id == teacher_id).first()

        if db_teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found")

        # Update the BDDemo column with new data using raw SQL
        query = text("""
            UPDATE teachers
            SET BDDemo = :bddemo
            WHERE id = :teacher_id
            RETURNING id, AnonymizedTeacherID, AnonymizedTeacherNumber, BDDemo
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
            BDDemo=bddemo
        )

        return response_teacher
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

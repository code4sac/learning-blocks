from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Enum, Column, Integer, String, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
from sqlalchemy.exc import IntegrityError
import os
import enum
from typing import Optional, List
from dotenv import load_dotenv
from models import RoleEnum, StudentInDB, PeopleInDB, get_db
from fastapi import FastAPI, HTTPException, Depends
# Load environment variables from .env file
load_dotenv()

# Define the database path
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

# Set up SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define FastAPI app
app = FastAPI()



class PeopleInDBCreate(BaseModel):
    name: str
    age: Optional[int] = None
    role: RoleEnum
    AnonymizedStudentID: str
    AnonymizedStudentNumber: Optional[str] = None
    AnonymizedCounselorNumber: Optional[str] = None
    AnonymizedHomeroomTeacherNumber: Optional[str] = None
    GraduationCohort: Optional[str] = None
    Birthdate: Optional[str] = None
    EnabledUser: Optional[str] = None
    Grades: Optional[List[str]] = None
    FamilyKey: Optional[List[str]] = None
    SectionsIDs: Optional[str] = None
    GradebookIDs: Optional[List[str]] = None
    DateLastModified: Optional[str] = None

class PeopleInDBResponse(PeopleInDBCreate):
    id: int

class StudentInDBCreate(BaseModel):
    anonymizedStudentID: str
    anonymizedStudentNumber: Optional[str] = None
    role: RoleEnum


class PeopleInDBResponse(PeopleInDBCreate):
    id: int

    class Config:
        from_attributes = True  
        

class StudentInDBResponse(StudentInDBCreate):
    id: int
    people: PeopleInDBResponse

    class Config:
        from_attributes = True





# Create the database tables
Base.metadata.create_all(bind=engine)

@app.post("/people/", response_model=PeopleInDBResponse)
def create_person(person: PeopleInDBCreate, db: Session = Depends(get_db)):
    try:
        db_person = PeopleInDB(
            name=person.name,
            age=person.age,
            role=person.role,
            AnonymizedStudentID=person.AnonymizedStudentID,
            AnonymizedStudentNumber=person.AnonymizedStudentNumber,
            AnonymizedCounselorNumber=person.AnonymizedCounselorNumber,
            AnonymizedHomeroomTeacherNumber=person.AnonymizedHomeroomTeacherNumber,
            GraduationCohort=person.GraduationCohort,
            Birthdate=person.Birthdate,
            EnabledUser=person.EnabledUser,
            Grades=person.Grades,
            FamilyKey=person.FamilyKey,
            SectionsIDs=person.SectionsIDs,
            GradebookIDs=person.GradebookIDs,
            DateLastModified=person.DateLastModified
        )
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        return db_person
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/people/{person_id}", response_model=PeopleInDBResponse)
def read_person(person_id: int):
    db = SessionLocal()
    try:
        db_person = db.query(PeopleInDB).filter(PeopleInDB.id == person_id).first()
        if db_person is None:
            raise HTTPException(status_code=404, detail="Person not found")
        return db_person
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    finally:
        db.close()

@app.post("/students/", response_model=StudentInDBCreate)
def create_student(student: StudentInDBCreate):
    db = SessionLocal()
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
    finally:
        db.close()
import enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Enum, Column, Integer, String, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.exc import IntegrityError
import os
from typing import Optional, List
from dotenv import load_dotenv
from typing import Generator
from sqlalchemy.orm import Session

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
# Pydantic models
class RoleEnum(str, enum.Enum):
    administrator = "administrator"
    aide = "aide"
    guardian = "guardian"
    parent = "parent"
    proctor = "proctor"
    relative = "relative"
    student = "student"
    teacher = "teacher"

class Price_pers_Studen(int, enum.Enum):
    ADA_monies_per_stu = 1800

 
    
    
class StudentInDB(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    AnonymizedStudentID: Mapped[str] = mapped_column(String, unique=True, nullable=False)  # Ensure this is unique
    AnonymizedStudentNumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), nullable=False)
    
    # ForeignKey and relationship to PeopleInDB
    people_id: Mapped[int] = mapped_column(Integer, ForeignKey("people.id"))
    people: Mapped["PeopleInDB"] = relationship("PeopleInDB", back_populates="student")
 

# Add the new SchoolsInDB model
class SchoolsInDB(Base):
    __tablename__ = "schools"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    school_code: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    school_name: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    zip_code: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    
    # Relationship to PeopleInDB
    people: Mapped[List["PeopleInDB"]] = relationship("PeopleInDB", back_populates="school")

# Update the PeopleInDB model to include the SchoolCode foreign key
class PeopleInDB(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), nullable=False)
    
    # Other columns
    AnonymizedStudentID: Mapped[str] = mapped_column(String, ForeignKey("students.anonymizedStudentID"), nullable=True)  # Foreign key
    AnonymizedStudentNumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    AnonymizedCounselorNumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    AnonymizedHomeroomTeacherNumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    GraduationCohort: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    Birthdate: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    EnabledUser: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    Grades: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    FamilyKey: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    SectionsIDs: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    GradebookIDs: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    DateLastModified: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    
    # Foreign key to SchoolsInDB
    school_code: Mapped[Optional[str]] = mapped_column(String, ForeignKey("schools.school_code"), nullable=True)
    
    # Relationship to SchoolsInDB
    school: Mapped["SchoolsInDB"] = relationship("SchoolsInDB", back_populates="people")
    
    # Relationship to StudentInDB
    student: Mapped["StudentInDB"] = relationship("StudentInDB", back_populates="people")
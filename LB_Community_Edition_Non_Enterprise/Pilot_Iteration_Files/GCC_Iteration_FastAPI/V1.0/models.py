import enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Enum, Column, Integer, String, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
from sqlalchemy.exc import IntegrityError
import os
import enum
from typing import Optional, List
from dotenv import load_dotenv


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
    
class StudentInDB(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    anonymizedStudentID: Mapped[str] = mapped_column(String, nullable=False)
    anonymizedStudentNumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), nullable=False)
    
    # ForeignKey and relationship to PeopleInDB
    people_id: Mapped[int] = mapped_column(Integer, ForeignKey("people.id"))
    people: Mapped["PeopleInDB"] = relationship("PeopleInDB", back_populates="student")

class PeopleInDB(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), nullable=False)
    
    # Other columns
    AnonymizedStudentID: Mapped[str] = mapped_column(String, nullable=False)
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
    
    # Relationship to StudentInDB
    student: Mapped["StudentInDB"] = relationship("StudentInDB", back_populates="people")

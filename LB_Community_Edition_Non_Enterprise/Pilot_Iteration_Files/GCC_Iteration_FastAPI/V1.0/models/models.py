import enum
import json
import os
from typing import Optional, List, Dict, Generator
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Enum as SQLAEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Mapped, mapped_column
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from dotenv import load_dotenv
from sqlalchemy import create_engine

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

class PricePerStudent(int, enum.Enum):
    ADA_monies_per_stu = 1800

# Updated PeopleInDB model with polymorphism
class PeopleInDB(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    firstname: Mapped[str] = mapped_column(String, index=True)  # Changed to lowercase
    lastname: Mapped[str] = mapped_column(String, index=True)  # Changed to lowercase
    role: Mapped[RoleEnum] = mapped_column(SQLAEnum(RoleEnum), nullable=False, index=True)
    sourcedid: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)  # sourcedid as the unique identifier
    enableduser: Mapped[str] = mapped_column(String, index=True)  # Changed to lowercase
    datelastmodified: Mapped[str] = mapped_column(String, index=True)  # Changed to lowercase
    school_code: Mapped[Optional[str]] = mapped_column(String, ForeignKey("schools.school_code"), nullable=True, index=True)
    
    # Relationships
    school: Mapped["SchoolsInDB"] = relationship("SchoolsInDB", back_populates="people")

    __mapper_args__ = {
        'polymorphic_on': role,  # This is the polymorphic discriminator
        'polymorphic_identity': 'people',  # Base identity
    }

# Polymorphic model for students
class StudentInDB(PeopleInDB):
    __tablename__ = "students"
    __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(Integer, ForeignKey("people.id"), primary_key=True, index=True)
    anonymizedstudentid: Mapped[str] = mapped_column(String, unique=True, nullable=False)  # Changed to lowercase
    anonymizedstudentnumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # Changed to lowercase
    bddemo: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)  # Changed to lowercase
    role: Mapped[RoleEnum] = mapped_column(SQLAEnum(RoleEnum), nullable=False, index=True)
    sourcedid: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    sections: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    schlassociated: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # Changed to lowercase
    birthdate: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # Changed to lowercase

    __mapper_args__ = {
        'polymorphic_identity': 'student',  # Identity for Student
    }

# Polymorphic model for teachers
def validate_stu_associated(data: Dict[str, Dict[str, Optional[str]]]) -> bool:
    """Validate the structure of StuAssociated data."""
    for key, value in data.items():
        if not isinstance(value, dict):
            return False
        if "Start_Date" not in value or "End_Date" not in value:
            return False
        if not isinstance(value["Start_Date"], (str, type(None))) or not isinstance(value["End_Date"], (str, type(None))):
            return False
    return True

class TeacherInDB(PeopleInDB):
    __tablename__ = "teachers"
    __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(Integer, ForeignKey("people.id"), primary_key=True, index=True)
    anonymizedteacherid: Mapped[str] = mapped_column(String, unique=True, nullable=False)  # Changed to lowercase
    anonymizedteachernumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # Changed to lowercase
    sections: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    stuassociated: Mapped[Optional[Dict[str, Dict[str, Optional[str]]]]] = mapped_column(JSON, nullable=True)  # Changed to lowercase
    schlassociated: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # Changed to lowercase
    credentials: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    subjects: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    siteduties: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    gradelevels: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    bddemo: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)  # Changed to lowercase

    def set_stu_associated(self, data: Optional[Dict[str, Dict[str, Optional[str]]]]):
        """Serialize dictionary to JSON string after validation."""
        if data and validate_stu_associated(data):
            self.stuassociated = json.dumps(data)
        else:
            raise ValueError("Invalid data structure for StuAssociated")

    def get_stu_associated(self) -> Optional[Dict[str, Dict[str, Optional[str]]]]:
        """Deserialize JSON string to dictionary."""
        return json.loads(self.stuassociated) if self.stuassociated else None

    __mapper_args__ = {
        'polymorphic_identity': 'teacher',  # Identity for Teacher
    }

# Add the SchoolsInDB model
class SchoolsInDB(Base):
    __tablename__ = "schools"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    school_code: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    school_name: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    zip_code: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    bddemo: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)  # Changed to lowercase

    # Relationship to PeopleInDB
    people: Mapped[List["PeopleInDB"]] = relationship("PeopleInDB", back_populates="school")

# Dependency to get DB session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

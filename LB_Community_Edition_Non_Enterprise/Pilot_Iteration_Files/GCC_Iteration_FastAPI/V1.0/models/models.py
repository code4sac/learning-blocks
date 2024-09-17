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
    ID: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    FirstName: Mapped[str] = mapped_column(String, index=True)
    LastName: Mapped[str] = mapped_column(String, index=True)
    Role: Mapped[RoleEnum] = mapped_column(SQLAEnum(RoleEnum), nullable=False, index=True)
    SourcedID: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    EnabledUser: Mapped[str] = mapped_column(String, index=True)
    DateLastModified: Mapped[str] = mapped_column(String, index=True)
    SchoolCode: Mapped[Optional[str]] = mapped_column(String, ForeignKey("schools.SchoolCode"), nullable=True, index=True)
    AnonymizedStudentID: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    AnonymizedStudentNumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    AnonymizedTeacherID: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    school: Mapped["SchoolsInDB"] = relationship("SchoolsInDB", back_populates="people")
    __mapper_args__ = {
        'polymorphic_on': Role,
        'polymorphic_identity': 'people',
    }


# Polymorphic model for students
class StudentInDB(PeopleInDB):
    __tablename__ = "students"
    __table_args__ = {'extend_existing': True}
    __mapper_args__ = {
        'polymorphic_identity': 'student',  # Identity for Teacher
        'inherit_condition': PeopleInDB.ID == id,  # Specify the inherit condition
    }
    id: Mapped[int] = mapped_column(Integer, ForeignKey("people.ID"), primary_key=True, index=True)
    AnonymizedStudentID: Mapped[str] = mapped_column(String, nullable=False) 
    AnonymizedStudentNumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    MetaData: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)
    Sections: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  
    SchlAssociated: Mapped[Optional[str]] = mapped_column(String,  nullable=True)
    StuAssociated: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)
    Birthdate: Mapped[Optional[str]] = mapped_column(String, nullable=True)  
    SchoolCode: Mapped[Optional[str]] = mapped_column(String, ForeignKey("schools.SchoolCode"), nullable=True, index=True)
    GradeLevels: Mapped[Optional[str]] = mapped_column(String, nullable=True)  
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
    __mapper_args__ = {
        'polymorphic_identity': 'teacher',  # Identity for Teacher
        'inherit_condition': PeopleInDB.ID == id,  # Specify the inherit condition
    }
    id: Mapped[int] = mapped_column(Integer, ForeignKey("people.ID"), primary_key=True, index=True)
    AnonymizedTeacherID: Mapped[str] = mapped_column(String, unique=True,  nullable=False)  # Changed to lowercase
    Sections: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    StuAssociated: Mapped[Optional[Dict[str, Dict[str, Optional[str]]]]] = mapped_column(JSON, nullable=True)  # Changed to lowercase
    SchlAssociated: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # Changed to lowercase
    Credentials: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    Subjects: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    SiteDuties: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)  # Changed to lowercase
    GradeLevels: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # Changed to lowercase
    MetaData: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)  # Changed to lowercase
    Role: Mapped[RoleEnum] = mapped_column(SQLAEnum(RoleEnum), nullable=False, index=True)
    SourcedID: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    SchoolCode: Mapped[Optional[str]] = mapped_column(String, ForeignKey("schools.SchoolCode"), nullable=True, index=True)
    EnabledUser: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # Changed to lowercase


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
    ID: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    SchoolCode: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    SchoolName: Mapped[str] = mapped_column(String, nullable=False)
    GradeLevels: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    Address: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    City: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    State: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    ZipCode: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    MetaData: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)  # Changed to lowercase
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

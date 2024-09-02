import enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Enum, Column, Integer, String, JSON, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, with_polymorphic
from sqlalchemy.exc import IntegrityError
import os
from typing import Optional, List, Generator, Dict
from dotenv import load_dotenv
from sqlalchemy.orm import Mapped, mapped_column

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
    Firstname: Mapped[str] = mapped_column(String, index=True)
    Lastname: Mapped[str] = mapped_column(String, index=True)
    role: Mapped[RoleEnum]= mapped_column(Enum(RoleEnum), nullable=False, index=True)
    sourcedid: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)  # sourcedid as the unique identifier
    EnabledUser: Mapped[str] = mapped_column(String, index=True)
    DateLastModified: Mapped[str] = mapped_column(String, index=True)

    # Foreign key to SchoolsInDB
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
    __table_args__ = {'extend_existing': True}  # Add this line
    id: Mapped[int] = mapped_column(Integer, ForeignKey("people.id"), primary_key=True, index=True)
    AnonymizedStudentID: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    AnonymizedStudentNumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    
    # Additional student-specific fields can be added here

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
    __table_args__ = {'extend_existing': True}  # Add this line
    id: Mapped[int] = mapped_column(Integer, ForeignKey("people.id"), primary_key=True, index=True)
    AnonymizedTeacherID: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    AnonymizedTeacherNumber: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    Sections: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)
    StuAssociated: Mapped[Optional[Dict[str, Dict[str, Optional[str]]]]] = mapped_column(JSON, nullable=True)
    SchlAssociated: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    Credentials: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)
    Subjects: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)
    SiteDuties: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)
    GradeLevels: Mapped[Optional[List[str]]] = mapped_column(String, nullable=True)
    BDDemo: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)
    BDGender: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)
    BDASTI: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)
    BDCCI: Mapped[Optional[Dict[str, List[str]]]] = mapped_column(JSON, nullable=True)

    def set_stu_associated(self, data: Optional[Dict[str, Dict[str, Optional[str]]]]):
        """Serialize dictionary to JSON string after validation."""
        if data and validate_stu_associated(data):
            import json
            self.StuAssociated = json.dumps(data)
        else:
            raise ValueError("Invalid data structure for StuAssociated")

    def get_stu_associated(self) -> Optional[Dict[str, Dict[str, Optional[str]]]]:
        """Deserialize JSON string to dictionary."""
        import json
        return json.loads(self.StuAssociated) if self.StuAssociated else None
    # Additional teacher-specific fields can be added here

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
    
    # Relationship to PeopleInDB
    people: Mapped[List["PeopleInDB"]] = relationship("PeopleInDB", back_populates="school")
# Utility functions
def serialize_to_json(data: Optional[Dict[str, List[str]]]) -> Optional[str]:
    if data is not None:
        return json.dumps(data)
    return None

def deserialize_from_json(data: Optional[str]) -> Optional[Dict[str, List[str]]]:
    if data is not None:
        return json.loads(data)
    return None

Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
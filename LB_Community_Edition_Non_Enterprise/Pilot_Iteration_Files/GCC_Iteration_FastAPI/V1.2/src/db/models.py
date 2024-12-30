from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy import Table, String, ForeignKey, Enum as SQLMEnum
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from typing import List, Optional, Dict
from enum import Enum
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.orm import declared_attr

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

class RoleEnum(str, Enum):
    administrator = "administrator"
    aide = "aide"
    guardian = "guardian"
    parent = "parent"
    proctor = "proctor"
    relative = "relative"
    student = "student"
    teacher = "teacher"

# Define the association table for the many-to-many relationship
student_section_association = Table(
    "student_section_association",
    SQLModel.metadata,
    Column("school_id", ForeignKey("schools.ID"), primary_key=True),
    Column("student_id", ForeignKey("students.ID"), primary_key=True),
    Column("section_id", ForeignKey("sections.ID"), primary_key=True)
)
class SchoolsInDB(SQLModel, table=True):
    __tablename__ = "schools"

    ID: int = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(unique=True, nullable=False)
    SchoolName: str = Field(nullable=False)
    GradeLevels: Optional[str] = Field(default=None)
    Address: Optional[str] = Field(default=None)
    City: Optional[str] = Field(default=None)
    State: Optional[str] = Field(default=None)
    ZipCode: Optional[str] = Field(default=None)
    MetaData: Optional[Dict[str, List[str]]] = Field(default=None, sa_column=Column(JSON))
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))

    # Add relationship to SectionsInDB
    sections: List["SectionsInDB"] = Relationship(back_populates="school")


class SectionsInDB(SQLModel, table=True):
    __tablename__ = "sections"

    ID: int = Field(default=None, primary_key=True, index=True)
    CourseName: str = Field(nullable=False)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    MetaData: Optional[Dict[str, List[str]]] = Field(default=None, sa_column=Column(JSON))
    students: List["StudentInDB"] = Relationship(back_populates="sections")

class BaseWithPolymorphism(SQLModel):
    """
    Base class that handles the polymorphic setup.
    This abstracts the common setup for polymorphic behavior.
    """
    
    @declared_attr
    def __mapper_args__(cls):
        return {
            "polymorphic_on": cls.__table__.c.role,
            "polymorphic_identity": cls.__name__.lower(),
        }


class PeopleInDB(BaseWithPolymorphism, table=True):
    __tablename__ = "people"

    ID: int = Field(default=None, primary_key=True, index=True)
    FirstName: str = Field(index=True)
    LastName: str = Field(index=True)

    Role: RoleEnum = Field(sa_column=Column(SQLMEnum(RoleEnum), nullable=False))

    SourcedID: str = Field(unique=True, nullable=False, index=True)
    EnabledUser: Optional[str] = Field(default=None, index=True)
    DateLastModified: Optional[str] = Field(default=None, index=True)
    SchoolCode: Optional[str] = Field(default=None, foreign_key="schools.SchoolCode", index=True)
    AnonymizedStudentID: Optional[str] = Field(default=None)
    AnonymizedStudentNumber: Optional[str] = Field(default=None)
    AnonymizedTeacherID: Optional[str] = Field(default=None, unique=True)

    # Relationship field
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")

    __mapper_args__ = {
        "polymorphic_identity": "people",
    }

    class Config:
        arbitrary_types_allowed = True


class StudentInDB(BaseWithPolymorphism, table=True):
    __tablename__ = "students"

    # Regular fields
    ID: int = Field(default=None, primary_key=True, foreign_key="people.ID", index=True)
    AnonymizedStudentID: str = Field(nullable=False)
    AnonymizedStudentNumber: Optional[str] = Field(default=None)
    MetaData: Optional[Dict[str, List[str]]] = Field(default=None, sa_column=Column(JSON))
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))

    sections: List["SectionsInDB"] = Relationship(back_populates="students")

    __mapper_args__ = {
        "polymorphic_identity": "student",
    }


class TeacherInDB(BaseWithPolymorphism, table=True):
    __tablename__ = "teachers"

    # Regular fields
    ID: int = Field(default=None, primary_key=True, foreign_key="people.ID", index=True)
    AnonymizedTeacherID: str = Field(nullable=False, unique=True)
    StuAssociated: Optional[Dict[str, Dict[str, Optional[str]]]] = Field(
        default=None, sa_column=Column(JSON)
    )
    Credentials: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    Subjects: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    GradeLevels: Optional[str] = Field(default=None)
    MetaData: Optional[Dict[str, List[str]]] = Field(default=None, sa_column=Column(JSON))
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    sections: List["SectionsInDB"] = Relationship(back_populates="teachers")

    # Relationships and additional methods
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
    
    __mapper_args__ = {
        "polymorphic_identity": "teacher",
    }

    def set_stu_associated(self, data: Optional[Dict[str, Dict[str, Optional[str]]]]):
        """Sets the StuAssociated field after validation."""
        if data and validate_stu_associated(data):
            self.StuAssociated = data
        else:
            raise ValueError("Invalid structure for StuAssociated")

    def get_stu_associated(self) -> Optional[Dict[str, Dict[str, Optional[str]]]]:
        """Returns the StuAssociated field as a dictionary."""
        return self.StuAssociated

    


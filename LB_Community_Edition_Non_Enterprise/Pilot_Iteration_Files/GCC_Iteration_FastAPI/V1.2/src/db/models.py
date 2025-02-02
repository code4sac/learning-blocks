from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy import String, Enum as SQLMEnum
from sqlalchemy.dialects.postgresql import JSON
from typing import List, Optional, Dict
from enum import Enum
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.orm import declared_attr
from pydantic import BaseModel
from sqlmodel import Field
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Integer, String, Enum as SQLAlchemyEnum, DateTime
from uuid import uuid4



# Polymorphic model for teachers
def validate_stu_associated(data: Dict[str, Dict[str, Optional[str]]]) -> bool:
    """Validate the structure of StuAssociated data."""
    for _, value in data.items():
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
    vendor = "vendor"

class LocationEnum(str, Enum):
    school = "school"
    district = "district"
    state = "state"

class CCIEnum(str, Enum):
    college = "college"
    career = "career"
    college_career = "college_career"

class IndicatorCategoryEnum(str, Enum):
    SED = "Socioeconomically Disadvantaged"
    EL = "English Learner"
    SWD = "Students with Disabilities"
    FosterYouth = "Foster Youth"
    Homeless = "Homeless"
    Migrant = "Migrant"
    White = "White"
    Hispanic = "Hispanic"
    AmericanIndianOrAlaskaNative = "American Indian or Alaska Native"
    Asian = "Asian"
    BlackOrAfricanAmerican = "Black or African American"
    NativeHawaiianOrOtherPacificIslander = "Native Hawaiian or Other Pacific Islander"
    TwoOrMoreRaces = "Two or More Races, Not Hispanic"

class ColorEnum(str, Enum):
    red = "red"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    blue = "blue"

class TrueFalseEnum(str, Enum):
    true = "true"
    false = "false"

class TimestampMixin:
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc), sa_column_kwargs={"onupdate": lambda: datetime.now(datetime.timezone.utc)})

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
# ✅ Abstract Base Class (No Table)
class ReadinessData:
  

    ReadinessLocation: LocationEnum = Field(nullable=False, index=True) 
    ReadinessCCI: CCIEnum = Field(  nullable=False, index=True)
    ReadinessIndicatorCategory: IndicatorCategoryEnum = Field( nullable=False, index=True)



# ✅ Subclasses with Unique Tables
class ReadinessTotalData(ReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_total_data"
    TotalID: int = Field(default=None, primary_key=True, index=True)
    TotalRate: str = Field(unique=True, nullable=False)


class ReadinessNumerator(ReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_numerator"
    NumeratorID: int = Field(default=None, primary_key=True, index=True)
    NumeratorRate: str = Field(unique=True, nullable=False)

class CCPerformanceColorData(ReadinessData, SQLModel, table=True):
    __tablename__ = "cc_performance_color_data"
    PerformanceID: int = Field(default=None, primary_key=True, index=True)
    PerformColor: str = Field( nullable=False)

class ReadinessStatusData(ReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_status_data"
    StatusID: int = Field(default=None, primary_key=True, index=True)
    StatusRate: str = Field( nullable=False)

class ReadinessDenominatorData(ReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_denominator_data"
    DenominatorID: int = Field(default=None, primary_key=True, index=True)
    DenominatorRate: str = Field( nullable=False)

class ReadinessChangeData(ReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_change_data"
    ChangeID: int = Field(default=None, primary_key=True, index=True)
    ChangeRate: str = Field( nullable=False)


class StudentSectionAssociation(TimestampMixin, SQLModel, table=True):
    __tablename__ = "student_section_association"

    school_id: int = Field(foreign_key="schools.SchoolID", primary_key=True)
    student_id: int = Field(foreign_key="students.StudentID", primary_key=True)
    section_id: int = Field(foreign_key="sections.SectionID", primary_key=True)
    teacher_id: int = Field(foreign_key="teachers.TeacherID", primary_key=True)
 
class SchoolsInDB(TimestampMixin, SQLModel, table=True):
    __tablename__ = "schools"

    SchoolID: int = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(unique=True, nullable=False)
    SchoolName: str = Field(nullable=False)
    GradeLevels: Optional[str] = Field(default=None)
    Address: Optional[str] = Field(default=None)
    City: Optional[str] = Field(default=None)
    State: Optional[str] = Field(default=None)
    ZipCode: Optional[str] = Field(default=None)
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
 
    school_readiness_status_data: List["ReadinessStatusData"] = Relationship(back_populates="school")
    school_performance_color_data: List["CCPerformanceColorData"] = Relationship(back_populates="school")
    school_readiness_change_data: List["ReadinessChangeData"] = Relationship(back_populates="school")
    school_readiness_total_data: List["ReadinessTotalData"] = Relationship(back_populates="school")
    school_readiness_numerator: List["ReadinessNumerator"] = Relationship(back_populates="school")
    school_readiness_denominator_data: List["ReadinessDenominatorData"] = Relationship(back_populates="school")
    

    # Add relationship to SectionsInDB
    sections: List["SectionsInDB"] = Relationship(back_populates="school")


class SectionsInDB(TimestampMixin,SQLModel, table=True):
    __tablename__ = "sections"

    SectionID: int = Field(default=None, primary_key=True, index=True)
    CourseName: str = Field(nullable=False)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    students: List["StudentInDB"] = Relationship(back_populates="sections")
 


class PeopleInDB(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "people"

    PeopleID: int = Field(default=None, primary_key=True, index=True)
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


class StudentInDB(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "students"

    # Regular fields
    StudentID: int = Field(default=None, primary_key=True, foreign_key="people.PeopleID", index=True)
    AnonymizedStudentID: str = Field(nullable=False)
    AnonymizedStudentNumber: Optional[str] = Field(default=None)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    sections: List["SectionsInDB"] = Relationship(back_populates="students")   
    Interventions: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))    
 
    
    # Define the relationships with ReadinessStatusData and PerformanceColorData
    student_readiness_status_data: List["ReadinessStatusData"] = Relationship(back_populates="school")
    student_performance_color_data: List["CCPerformanceColorData"] = Relationship(back_populates="school")
    student_readiness_change_data: List["ReadinessChangeData"] = Relationship(back_populates="school")
    student_readiness_total_data: List["ReadinessTotalData"] = Relationship(back_populates="school")
    student_readiness_numerator: List["ReadinessNumerator"] = Relationship(back_populates="school")
    student_readiness_denominator_data: List["ReadinessDenominatorData"] = Relationship(back_populates="school")
    
    __mapper_args__ = {
        "polymorphic_identity": "student",
    }


class TeacherInDB(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "teachers"

    # Regular fields
    TeacherID: int = Field(default=None, primary_key=True, foreign_key="people.PeopleID", index=True)
    AnonymizedTeacherID: str = Field(nullable=False, unique=True)
    StuAssociated: Optional[Dict[str, Dict[str, Optional[str]]]] = Field(
        default=None, sa_column=Column(JSON)
    )
    Credentials: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    Subjects: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
    GradeLevels: Optional[str] = Field(default=None)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
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
    
class class_section(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "class_section"

    # Regular fields
    ClassSectionID: int = Field(default=None, primary_key=True, index=True)
    SectionName: str = Field(nullable=False)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
 
    __mapper_args__ = {
        "polymorphic_identity": "class_section",
    }

class Vendor(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "vendors"

    # Regular fields
    VendorID: int = Field(default=None, primary_key=True, foreign_key="people.PeopleID", index=True)
    VendorName: str = Field(nullable=False)
    VendorURL: str = Field(nullable=False)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
 
    # Relationships
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")

    __mapper_args__ = {
        "polymorphic_identity": "vendor",
    }

class Config:
            arbitrary_types_allowed = True

class InterventionCategories(TimestampMixin, BaseWithPolymorphism, table=True):
        __tablename__ = "intervention_categories"

        # Regular fields
        InterventionCategoriesID: int = Field(default=None, primary_key=True, index=True)
        CategoryName: str = Field(nullable=False)
        MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))

        # Relationships
        school: Optional["SchoolsInDB"] = Relationship(back_populates="people")

        __mapper_args__ = {
            "polymorphic_identity": "intervention_categories",
        }

class InterventionSession(TimestampMixin, BaseWithPolymorphism, table=True):
        __tablename__ = "interventions"

        # Regular fields
        InterventionSessionID: int = Field(default=None, primary_key=True, index=True)
        Intervention_Category: Optional[int] = Field(default=None, foreign_key="intervention_categories.InterventionCategoriesID", primary_key=True)
        InterventionSessionName: str = Field(nullable=False)
        MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
        Vendor: Optional[int] = Field(nullable=False, foreign_key="vendors.VendorID", index=True)
        Teacher: Optional[int] = Field(nullable=False, foreign_key="teachers.TeacherID", index=True)   
        student_id: Optional[int] = Field(default=None, foreign_key="students.StudentID", primary_key=True)
        school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
        created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))
        updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc), sa_column_kwargs={"onupdate": lambda: datetime.now(datetime.timezone.utc)})

        __mapper_args__ = {
            "polymorphic_identity": "interventions",
        }

class Config:
    arbitrary_types_allowed = True

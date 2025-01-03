from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy import Table, String, ForeignKey, Enum as SQLMEnum
from sqlalchemy.dialects.postgresql import JSON, ARRAY
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

class TimestampMixin:
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc), sa_column_kwargs={"onupdate": lambda: datetime.now(datetime.timezone.utc)})

# Define a model for the 'PerformanceColor' metadata
class CCPerformanceColorData(TimestampMixin, SQLModel, table=True):
    __tablename__ = "CC_performance_color_data"

    ID: str = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    Academic_Year: Optional[str] = None
    State_College_Career_Readiness_Performance_Color: Optional[int] = None
    School_College_Career_Readiness_Performance_Color: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_SED: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_EL: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_White: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_Hispanic: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_NA: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_Asi: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_AA: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_PAC: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_Fil: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_Two: Optional[int] = None
    School_College_Career_Readiness_Performance_Color_McVento: Optional[int] = None
    # Define the relationship with the SchoolsInDB table
    school: "SchoolsInDB" = Relationship(back_populates="performance_color_data")


# Define a model for the 'ReadinessStatus' metadata
class ReadinessStatusData(TimestampMixin, SQLModel, table=True):
    __tablename__ = "readiness_status_data"
    # Predefined keys for the readiness status data
    ID: str = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    Academic_Year: Optional[str] = None
    State_College_Career_Readiness_Status: Optional[int] = None
    School_College_Career_Readiness_Status: Optional[int] = None
    State_College_Career_Readiness_Rate: Optional[int] = None
    School_College_Career_Readiness_Rate: Optional[int] = None
    School_College_Career_Readiness_Rate_SED: Optional[int] = None
    School_College_Career_Readiness_Rate_EL: Optional[int] = None
    School_College_Career_Readiness_Rate_White: Optional[int] = None
    School_College_Career_Readiness_Rate_Hispanic: Optional[int] = None
    School_College_Career_Readiness_Rate_AA: Optional[int] = None
    School_College_Career_Readiness_Rate_Asi: Optional[int] = None
    School_College_Career_Readiness_Rate_PAC: Optional[int] = None
    School_College_Career_Readiness_Rate_Fil: Optional[int] = None
    School_College_Career_Readiness_Rate_Two: Optional[int] = None
    School_College_Career_Readiness_Rate_McVento: Optional[int] = None
    # Relationship to students (Optional list of students)
    school: "SchoolsInDB" = Relationship(back_populates="readiness_status_data")

    students: List["StudentInDB"] = Relationship(back_populates="readiness_status_data")

    def add_valid_students(self, session: sessionmaker, student_ids: List[int]):
        """Filter and add valid students to the readiness status data."""
        # Query the StudentInDB table to get the students with valid IDs
        valid_students = (
            session.execute(select(StudentInDB).filter(StudentInDB.ID.in_(student_ids)))
            .scalars()
            .all()
        )

        # Update the students relationship field
        self.students = valid_students


# Define a model for the 'ReadinessStatus' metadata
class ReadinessNumerator(TimestampMixin, SQLModel, table=True):
    __tablename__ = "readiness_numerator_data"
    # Predefined keys for the readiness status data
    ID: str = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    Academic_Year: Optional[str] = None
    
    # Adding the new fields for the readiness status numerators
    State_College_Career_Readiness_Numerator: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_SED: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_EL: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_White: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_Hispanic: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_AA: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_Asi: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_PAC: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_Fil: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_Two: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_McVento: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Numerator_At_Risk: Optional[int] = Field(default=0)
    
    # Relationship to students (Optional list of students)
    school: "SchoolsInDB" = Relationship(back_populates="readiness_numerator_data")
    students: List["StudentInDB"] = Relationship(back_populates="readiness_numerator_data")

    def add_valid_students(self, session: sessionmaker, student_ids: List[int]):
        """Filter and add valid students to the readiness status data."""
        # Query the StudentInDB table to get the students with valid IDs
        valid_students = (
            session.execute(select(StudentInDB).filter(StudentInDB.ID.in_(student_ids)))
            .scalars()
            .all()
        )

        # Update the students relationship field
        self.students = valid_students

    class Config:
        arbitrary_types_allowed = True
# Define a model for the 'ReadinessDenominator' metadata
class ReadinessDenominatorData(TimestampMixin, SQLModel, table=True):
    __tablename__ = "readiness_denominator_data"
    # Predefined keys for the readiness denominator data
    ID: str = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    Academic_Year: Optional[str] = None
    
    # Adding the new fields for the readiness denominator numerators
    State_College_Career_Readiness_Denominator: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_SED: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_EL: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_White: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_Hispanic: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_AA: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_Asi: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_PAC: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_Fil: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_Two: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_McVento: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Denominator_At_Risk: Optional[int] = Field(default=0)
    
    # Relationship to students (Optional list of students)
    school: "SchoolsInDB" = Relationship(back_populates="readiness_denominator_data")
    students: List["StudentInDB"] = Relationship(back_populates="readiness_denominator_data")

    def add_valid_students(self, session: sessionmaker, student_ids: List[int]):
        """Filter and add valid students to the readiness denominator data."""
        # Query the StudentInDB table to get the students with valid IDs
        valid_students = (
            session.execute(select(StudentInDB).filter(StudentInDB.ID.in_(student_ids)))
            .scalars()
            .all()
        )

        # Update the students relationship field
        self.students = valid_students

    class Config:
        arbitrary_types_allowed = True


# Define a model for the 'ReadinessChange' metadata
class ReadinessChangeData(TimestampMixin, SQLModel, table=True):
    __tablename__ = "readiness_change_data"
    # Predefined keys for the readiness change data
    ID: str = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    Academic_Year: Optional[str] = None
    StudentInDB: Optional[str] = Field(nullable=False, foreign_key="students.ID", index=True)  
    # Adding fields for the readiness change data
    State_College_Career_Readiness_Change: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Change: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Change_SED: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Change_EL: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Change_White: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Change_Hispanic: Optional[int] = Field(default=0)
    School_College_Readiness_Change_AA: Optional[int] = Field(default=0)
    School_College_Readiness_Change_Asi: Optional[int] = Field(default=0)
    School_College_Readiness_Change_PAC: Optional[int] = Field(default=0)
    School_College_Readiness_Change_Fil: Optional[int] = Field(default=0)
    School_College_Readiness_Change_Two: Optional[int] = Field(default=0)
    School_College_Readiness_Change_McVento: Optional[int] = Field(default=0)
    School_College_Readiness_Change_At_Risk: Optional[int] = Field(default=0)
    
    # Relationship to students (Optional list of students)
    school: "SchoolsInDB" = Relationship(back_populates="readiness_change_data")
    students: List["StudentInDB"] = Relationship(back_populates="readiness_change_data")

    def add_valid_students(self, session: sessionmaker, student_ids: List[int]):
        """Filter and add valid students to the readiness change data."""
        # Query the StudentInDB table to get the students with valid IDs
        valid_students = (
            session.execute(select(StudentInDB).filter(StudentInDB.ID.in_(student_ids)))
            .scalars()
            .all()
        )

        # Update the students relationship field
        self.students = valid_students

    class Config:
        arbitrary_types_allowed = True
# Define a model for the 'ReadinessTotal' metadata
class ReadinessTotalData(TimestampMixin, SQLModel, table=True):
    __tablename__ = "readiness_total_data"
    # Predefined keys for the readiness total data
    ID: str = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    Academic_Year: Optional[str] = None
    
    # Adding fields for the readiness total data
    State_College_Career_Readiness_Total: Optional[int] = Field(default=0)
    School_College_Readiness_Total: Optional[int] = Field(default=0)
    School_Career_Readiness_Total: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Total_AA: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Total_Asi: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Total_HIS: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Total_PAC: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Total_White: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Total_Two: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Total_McVento: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Total_SED: Optional[int] = Field(default=0)
    School_College_Career_Readiness_Total_EL: Optional[int] = Field(default=0)
    
    # Relationship to students (Optional list of students)
    school: "SchoolsInDB" = Relationship(back_populates="readiness_total_data")
    students: List["StudentInDB"] = Relationship(back_populates="readiness_total_data")

    def add_valid_students(self, session: sessionmaker, student_ids: List[int]):
        """Filter and add valid students to the readiness total data."""
        # Query the StudentInDB table to get the students with valid IDs
        valid_students = (
            session.execute(select(StudentInDB).filter(StudentInDB.ID.in_(student_ids)))
            .scalars()
            .all()
        )

        # Update the students relationship field
        self.students = valid_students

    class Config:
        arbitrary_types_allowed = True
# Define a model for the 'ReadinessTotal' metadata


class StudentSectionAssociation(TimestampMixin, SQLModel, table=True):
    __tablename__ = "student_section_association"

    school_id: int = Field(foreign_key="schools.ID", primary_key=True)
    student_id: int = Field(foreign_key="students.ID", primary_key=True)
    section_id: int = Field(foreign_key="sections.ID", primary_key=True)
    teacher_id: int = Field(foreign_key="teachers.ID", primary_key=True)

class SchoolsInDB(TimestampMixin, SQLModel, table=True):
    __tablename__ = "schools"

    ID: int = Field(default=None, primary_key=True, index=True)
    SchoolCode: str = Field(unique=True, nullable=False)
    SchoolName: str = Field(nullable=False)
    GradeLevels: Optional[str] = Field(default=None)
    Address: Optional[str] = Field(default=None)
    City: Optional[str] = Field(default=None)
    State: Optional[str] = Field(default=None)
    ZipCode: Optional[str] = Field(default=None)
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))
 
    # Define the relationships with ReadinessStatusData and PerformanceColorData
    readiness_status_data: List["ReadinessStatusData"] = Relationship(back_populates="school")
    performance_color_data: List["PerformanceColorData"] = Relationship(back_populates="school")
    readiness_change_data: List["ReadinessChangeData"] = Relationship(back_populates="school")
    readiness_total_data: List["ReadinessTotalData"] = Relationship(back_populates="school")
    readiness_numerator: List["ReadinessNumerator"] = Relationship(back_populates="school")
    readiness_denominator_data: List["ReadinessDenominatorData"] = Relationship(back_populates="school")
    

    # Add relationship to SectionsInDB
    sections: List["SectionsInDB"] = Relationship(back_populates="school")


class SectionsInDB(TimestampMixin,SQLModel, table=True):
    __tablename__ = "sections"

    ID: int = Field(default=None, primary_key=True, index=True)
    CourseName: str = Field(nullable=False)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
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


class PeopleInDB(TimestampMixin, BaseWithPolymorphism, table=True):
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


class StudentInDB(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "students"

    # Regular fields
    ID: int = Field(default=None, primary_key=True, foreign_key="people.ID", index=True)
    AnonymizedStudentID: str = Field(nullable=False)
    AnonymizedStudentNumber: Optional[str] = Field(default=None)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    Sections: Optional[List[str]] = Field(default=None, sa_column=Column(pg.ARRAY(String)))

    sections: List["SectionsInDB"] = Relationship(back_populates="students")

    __mapper_args__ = {
        "polymorphic_identity": "student",
    }


class TeacherInDB(TimestampMixin, BaseWithPolymorphism, table=True):
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
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
class BaseReadinessData(TimestampMixin):
    most_recent: Optional[bool] = Field(default=False)



class CCPerformanceColorData(BaseReadinessData, SQLModel, table=True):
    __tablename__ = "CC_performance_color_data"

    PerformID: str = Field(default=None, primary_key=True, index=True)
    PerformSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    PeformAcademicYear: Optional[str] = Field(default=None, index=True)
    PerformLocation: LocationEnum = Field(sa_column=Column(SQLMEnum(LocationEnum), nullable=False, index=True))
    PerformCCI: CCIEnum = Field(sa_column=Column(SQLMEnum(CCIEnum), nullable=False, index=True))
    PerformIndicatorCategory: IndicatorCategoryEnum = Field(sa_column=Column(SQLMEnum(IndicatorCategoryEnum), nullable=False, index=True))
    PerformColor:ColorEnum = Field(sa_column=Column(SQLMEnum(ColorEnum), nullable=False, index=True))
    # Define the relationship with the SchoolsInDB table
    Performschool: "SchoolsInDB" = Relationship(back_populates="performance_color_data")
    OfficialPerformanceColor:  Optional[TrueFalseEnum] = Field(default=None, index=True)


# Define a model for the 'ReadinessStatus' metadata
class ReadinessStatusData(BaseReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_status_data"
    # Predefined keys for the readiness status data
    ReadinessStatusID: str = Field(default=None, primary_key=True, index=True)
    ReadinessStatusSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    ReadinessStatusAcademicYear: Optional[str] = Field(default=None, index=True)
    ReadinessStatusLocation: LocationEnum = Field(sa_column=Column(SQLMEnum(LocationEnum), nullable=False, index=True))
    ReadinessStatusCCI: CCIEnum = Field(sa_column=Column(SQLMEnum(CCIEnum), nullable=False, index=True))
    ReadinessStatusmIndicatorCategory: IndicatorCategoryEnum = Field(sa_column=Column(SQLMEnum(IndicatorCategoryEnum), nullable=False, index=True))
    ReadinessStatusRate:ColorEnum = Field(sa_column=Column(SQLMEnum(ColorEnum), nullable=False, index=True))
    # Relationship to students (Optional list of students)
    OfficialReadinessStatus:  Optional[TrueFalseEnum] = Field(default=None, index=True)
    ReadinessStatusschool: "SchoolsInDB" = Relationship(back_populates="readiness_status_data")
 

    ReadinessStatusstudents: List["StudentInDB"] = Relationship(back_populates="readiness_change_data")

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
class ReadinessNumerator(BaseReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_numerator_data"
    # Predefined keys for the readiness status data
     
    ReadinessNumeratorID: str = Field(default=None, primary_key=True, index=True)
    ReadinessNumeratorSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    ReadinessNumeratorAcademicYear: Optional[str] = Field(default=None, index=True)
    ReadinessNumeratorLocation: LocationEnum = Field(sa_column=Column(SQLMEnum(LocationEnum), nullable=False, index=True))
    ReadinessNumeratorCCI: CCIEnum = Field(sa_column=Column(SQLMEnum(CCIEnum), nullable=False, index=True))
    ReadinessNumeratormIndicatorCategory: IndicatorCategoryEnum = Field(sa_column=Column(SQLMEnum(IndicatorCategoryEnum), nullable=False, index=True))
    ReadinessNumeratorRate:ColorEnum = Field(sa_column=Column(SQLMEnum(ColorEnum), nullable=False, index=True))
    OfficialReadinessNumerator:  Optional[TrueFalseEnum] = Field(default=None, index=True)
    # Relationship to students (Optional list of students)
    ReadinessNumeratorschool: "SchoolsInDB" = Relationship(back_populates="readiness_status_data")
 


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
class ReadinessDenominatorData(BaseReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_denominator_data"
    # Predefined keys for the readiness denominator data
    ReadinessDenominatorID: str = Field(default=None, primary_key=True, index=True)
    ReadinessDenominatorSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    ReadinessDenominatorAcademic_Year: Optional[str] = None
    ReadinessDenominatorID: str = Field(default=None, primary_key=True, index=True)
    ReadinessDenominatorSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    ReadinessDenominatorAcademicYear: Optional[str] = Field(default=None, index=True)
    ReadinessDenominatorLocation: LocationEnum = Field(sa_column=Column(SQLMEnum(LocationEnum), nullable=False, index=True))
    ReadinessDenominatorCCI: CCIEnum = Field(sa_column=Column(SQLMEnum(CCIEnum), nullable=False, index=True))
    ReadinessDenominatormIndicatorCategory: IndicatorCategoryEnum = Field(sa_column=Column(SQLMEnum(IndicatorCategoryEnum), nullable=False, index=True))
    ReadinessDenominatorRate:ColorEnum = Field(sa_column=Column(SQLMEnum(ColorEnum), nullable=False, index=True))
    OfficialReadinessDenominator:  Optional[TrueFalseEnum] = Field(default=None, index=True)
    # Relationship to students (Optional list of students)

    ReadinessDenominatorschool: "SchoolsInDB" = Relationship(back_populates="readiness_denominator_data")
    ReadinessDenominatorstudents: List["StudentInDB"] = Relationship(back_populates="readiness_denominator_data")

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
class ReadinessChangeData(BaseReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_change_data"
    ReadinessChangeID: str = Field(default=None, primary_key=True, index=True)
    ReadinessChangeSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    ReadinessChangeAcademic_Year: Optional[str] = None
    ReadinessChangeID: str = Field(default=None, primary_key=True, index=True)
    ReadinessChangeSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    ReadinessChangeAcademicYear: Optional[str] = Field(default=None, index=True)
    ReadinessChangeLocation: LocationEnum = Field(sa_column=Column(SQLMEnum(LocationEnum), nullable=False, index=True))
    ReadinessChangeCCI: CCIEnum = Field(sa_column=Column(SQLMEnum(CCIEnum), nullable=False, index=True))
    ReadinessChangeIndicatorCategory: IndicatorCategoryEnum = Field(sa_column=Column(SQLMEnum(IndicatorCategoryEnum), nullable=False, index=True))
    ReadinessChangeRate:ColorEnum = Field(sa_column=Column(SQLMEnum(ColorEnum), nullable=False, index=True))
    OfficialReadinessChange:  Optional[TrueFalseEnum] = Field(default=None, index=True)
    
    # Relationship to students (Optional list of students)
    ReadinessChangeschool: "SchoolsInDB" = Relationship(back_populates="readiness_change_data")
    ReadinessChangestudents: List["StudentInDB"] = Relationship(back_populates="readiness_change_data")

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
class ReadinessTotalData(BaseReadinessData, SQLModel, table=True):
    __tablename__ = "readiness_total_data"
    # Predefined keys for the readiness total data
    ReadinessTotalID: str = Field(default=None, primary_key=True, index=True)
    ReadinessTotalSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    ReadinessTotalAcademic_Year: Optional[str] = None
    ReadinessTotalID: str = Field(default=None, primary_key=True, index=True)
    ReadinessTotalSchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    ReadinessTotalAcademicYear: Optional[str] = Field(default=None, index=True)
    ReadinessTotalLocation: LocationEnum = Field(sa_column=Column(SQLMEnum(LocationEnum), nullable=False, index=True))
    ReadinessTotalCCI: CCIEnum = Field(sa_column=Column(SQLMEnum(CCIEnum), nullable=False, index=True))
    ReadinessTotalIndicatorCategory: IndicatorCategoryEnum = Field(sa_column=Column(SQLMEnum(IndicatorCategoryEnum), nullable=False, index=True))
    ReadinessTotalRate:ColorEnum = Field(sa_column=Column(SQLMEnum(ColorEnum), nullable=False, index=True))
    OfficialReadinessTotal:  Optional[TrueFalseEnum] = Field(default=None, index=True)
    
    # Relationship to students (Optional list of students)
    ReadinessTotalschool: "SchoolsInDB" = Relationship(back_populates="readiness_total_data")
    # Define the relationship to the junction table
    ReadinessTotalstudents: List["StudentInDB"] = Relationship(back_populates="readiness_total_data")


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

    ID: int = Field(default=None, primary_key=True, index=True)
    CourseName: str = Field(nullable=False)
    SchoolCode: str = Field(nullable=False, foreign_key="schools.SchoolCode", index=True)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    students: List["StudentInDB"] = Relationship(back_populates="sections")
 


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
    
class class_section(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "class_section"

    # Regular fields
    ID: int = Field(default=None, primary_key=True, index=True)
    SectionName: str = Field(nullable=False)
    MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
    school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
 
    __mapper_args__ = {
        "polymorphic_identity": "class_section",
    }

class Vendor(TimestampMixin, BaseWithPolymorphism, table=True):
    __tablename__ = "vendors"

    # Regular fields
    ID: int = Field(default=None, primary_key=True, foreign_key="people.ID", index=True)
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
        ID: int = Field(default=None, primary_key=True, index=True)
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
        ID: int = Field(default=None, primary_key=True, index=True)
        Intervention_Category: Optional[int] = Field(default=None, foreign_key="intervention_categories.ID", primary_key=True)
        InterventionSessionName: str = Field(nullable=False)
        MetaData: Optional[Dict[str, BaseModel]] = Field(default=None, sa_column=Column(JSON))
        Vendor: Optional[int] = Field(nullable=False, foreign_key="vendors.ID", index=True)
        Teacher: Optional[int] = Field(nullable=False, foreign_key="teachers.ID", index=True)   
        student_id: Optional[int] = Field(default=None, foreign_key="students.ID", primary_key=True)
        school: Optional["SchoolsInDB"] = Relationship(back_populates="people")
        created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))
        updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(datetime.timezone.utc), sa_column_kwargs={"onupdate": lambda: datetime.now(datetime.timezone.utc)})

        __mapper_args__ = {
            "polymorphic_identity": "interventions",
        }

class Config:
    arbitrary_types_allowed = True

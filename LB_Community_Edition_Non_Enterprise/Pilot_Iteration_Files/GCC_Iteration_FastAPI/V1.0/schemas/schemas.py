from typing import Optional, List, Union, Dict, Optional
from models.models import RoleEnum
from pydantic import BaseModel, Field

# Base schema for PeopleInDB creation
class PeopleInDBCreate(BaseModel):
    Firstname: str
    Lastname: str
    role: RoleEnum
    sourcedid: str  # Unique identifier for linking
    EnabledUser: str = "True"
    DateLastModified: Optional[str] = None
    school_code: Optional[str] = None  # Field for SchoolCode

    class Config:

        from_attributes = True

# Base schema for StudentInDB creation
class StudentInDBCreate(BaseModel):
    AnonymizedStudentID: str
    AnonymizedStudentNumber: Optional[str] = None
    role: RoleEnum = "student"
    sourcedid: str  # This will link to PeopleInDB's sourcedid

    class Config:
        from_attributes = True

class BDDemoModel(BaseModel):
    BDcurrentAcademicIndicator: Dict[str, int] = Field(
        {
            "Suspensions_Indicator": 0,
            "EL_Prgrs_Indicator": 0,
            "Grad_Rate_Indicator": 0,
            "College_Career_Indicator": 0,
            "ELA_Indicator": 0,
            "Math_Indicator": 0,
            "Total_Students_Grad_OnTrack": 0,
            "Total_Students_Grad_OffTrack": 0,
            "Total_At_Risk_Students": 0,
        },
        description="Breakdown of students by academic indicators."
    )
    BDcurrentethnicity: Dict[str, int] = Field(
        {
            "Total_Hispanic": 0,
            "Total_White_Hispanic": 0,
            "Total_None_White_Hispanic": 0,
        },
        description="Breakdown of students by ethnicity with total counts."
    )
    BDcurrentrace: Dict[str, int] = Field(
        {
            "Total_American_Indian_Alaska_Native": 0,
            "Total_Native_Hawaiian_Other_Pacific_Islander": 0,
            "Total_White": 0,
            "Total_Black_African_American": 0,
            "Total_Asian": 0,
            "Total_Filipino": 0,
            "Total_Hispanic": 0,
            "Total_Pacific_Islander": 0,
            "Total_Two_or_more": 0,
        },
        description="Breakdown of students by race with total counts."
    )
    BDcurrentgender: Dict[str, int] = Field(
        {
            "Total_Students": 0,
            "Total_Male_Students": 0,
            "Total_Female_Students": 0,
            "Total_Non-Binary_Students": 0,
        },
        description="Breakdown of students by gender with total counts."
    )
    BDcurrentSPED: Dict[str, int] = Field(
        {
            "Total_IEP_Students": 0,
            "Total_504_Students": 0,
            "Total_Students_with_Disabilities": 0,
            "Total_Students_without_Disabilities": 0,
            "Total_Students": 0,
        }
    )
    BDcurrentLangAcq: Dict[str, int] = Field(
        {
            "Total_English_Learners": 0,
            "Total_English_Proficient": 0,
            "Total_Long_Term_English_Learners": 0,
            "Total_Reclassified_Fluent_English_Proficient": 0,
            "Total_Students": 0,
        }
    )
    BDcurrentSpclPrg: Dict[str, int] = Field(
        {
            "Total_Free_Lunch": 0,
            "Total_Reduced_Lunch": 0,
            "Total_Pay_Lunch": 0,
            "Total_Mckinney_Vento": 0,
            "Total_Foster": 0,
            "Total_Socio_Econ_Disad": 0,
            "Total_Students": 0,
            "Total_At_Risk": 0,
        }
    )
    BDcurrentAtRiskIndicators: Dict[str, int] = Field(
        {
            "Total_Free_Lunch": 0,
            "Total_Reduced_Lunch": 0,
            "Total_Pay_Lunch": 0,
            "Total_Mckinney_Vento": 0,
            "Total_Foster": 0,
            "Total_Socio_Econ_Disad": 0,
            "Total_Students": 0,
            "Total_At_Risk": 0,
        }
    )
    BDcurrentAttendance: Dict[str, int] = Field(
        {
            "Total_Days_Absent": 0,
            "Total_Days_Present": 0,
            "Total_Days_InSchl_Suspended": 0,
            "Total_Days_Home_Suspended": 0,
            "Total_Students_Chronically_Absent": 0,
            "Total_Students_Not_Chronically_Absent": 0,
            "Total_Students_Mid_Year_Graduated": 0,
            "Total_Students_Mid_Year_Enrolled": 0,
            "Total_Students_Admin_Dropped": 0,
            "Total_Students": 0,
        }
    )
    BDcurrentRetention: Dict[str, int] = Field(
        {
            "Total_Students_Retained": 0,
            "Total_Students": 0,
        }
    )
    BDcurrentSuspensions: Dict[str, int] = Field(
        {
            "Total_Suspensions": 0,
            "Total_Students": 0,
        }
    )


class TeacherInDBCreate(BaseModel):
    AnonymizedTeacherID: str
    AnonymizedTeacherNumber: Optional[str] = None
    Sections: Optional[List[str]] = None
    StuAssociated: Optional[List[str]] = None
    SchlAssociated: Optional[str] = None
    Credentials: Optional[List[str]] = None
    Subjects: Optional[List[str]] = None
    SiteDuties: Optional[List[str]] = None
    GradeLevels: Optional[List[str]] = None
    BDDemo: Optional[BDDemoModel] = None

    class Config:
        from_attributes = True

# Response schema for PeopleInDB


# Response schema for StudentInDB
class StudentInDBResponse(StudentInDBCreate):
    AnonymizedStudentID: str
    AnonymizedStudentNumber: Optional[str] = None
    role: RoleEnum = "student"
    sourcedid: str
    id: int

    class Config:
      from_attributes = True

# Response schema for TeacherInDB
class TeacherInDBResponse(TeacherInDBCreate):
    AnonymizedTeacherID: str
    AnonymizedTeacherNumber: Optional[str] = None
    role: RoleEnum = "teacher"
    sourcedid: str
    StuAssociated: List[StudentInDBResponse] = []
    SchlAssociated: Optional[str] = None
    Credentials: Optional[List[str]] = None
    Subjects: Optional[List[str]] = None
    SiteDuties: Optional[List[str]] = None
    GradeLevels: Optional[List[str]] = None


    class Config:
      from_attributes = True


class PeopleInDBResponse(PeopleInDBCreate):
   id: int
   Firstname: str
   Lastname: str
   role: RoleEnum = "RoleEnum"
   sourcedid: str
   EnabledUser: Optional[str] = None
   DateLastModified: Optional[str] = None
   school_code: Optional[str] = None
    
   # Include related models based on the role
   student: Optional[StudentInDBResponse] = None
   teacher: Optional[TeacherInDBResponse] = None
   class Config:
       from_attributes = True
# Base schema for SchoolsInDB

class SchoolsInDBBase(BaseModel):
    school_code: str
    school_name: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None

    class Config:
        orm_mode = True

# Schema for SchoolsInDB creation
class SchoolsInDBCreate(SchoolsInDBBase):
    pass

# Response schema for SchoolsInDB
class SchoolsInDB(SchoolsInDBBase):
    id: int
    people: List[PeopleInDBResponse]  # List of people associated with the school

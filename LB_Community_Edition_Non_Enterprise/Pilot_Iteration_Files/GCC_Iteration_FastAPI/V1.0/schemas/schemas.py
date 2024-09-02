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
            # Add any other predefined keys you need here
        },
        description="Breakdown of students by race with total counts."
    )
 BDcurrentgender: Dict[str, int] = Field(
        {
            "Total_Students": 0,
            "Total_Male_Students": 0,
            "Total_Female_Students": 0,
        },

        description="Breakdown of students by ethnicity with total counts."
    )
class BDGenderModel(BaseModel):
    key1: List[str] = Field(..., description="Description for key1")
    key2: List[str] = Field(..., description="Description for key2")

class BDASTIModel(BaseModel):
    key1: List[str] = Field(..., description="Description for key1")
    key2: List[str] = Field(..., description="Description for key2")

class BDCCIModel(BaseModel):
    key1: List[str] = Field(..., description="Description for key1")
    key2: List[str] = Field(..., description="Description for key2")

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
    BDGender: Optional[BDGenderModel] = None
    BDASTI: Optional[BDASTIModel] = None
    BDCCI: Optional[BDCCIModel] = None
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
    id: int
    students: List[StudentInDBResponse] = []

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

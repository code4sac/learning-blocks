
from typing import Optional, List
from pydantic import BaseModel
from models.models import RoleEnum 
        
class PeopleInDBCreate(BaseModel):
    name: str
    age: Optional[int] = None
    role: RoleEnum
    AnonymizedStudentID: str
    AnonymizedStudentNumber: Optional[str] = None
    AnonymizedCounselorNumber: Optional[str] = None
    AnonymizedHomeroomTeacherNumber: Optional[str] = None
    GraduationCohort: Optional[str] = None
    Birthdate: Optional[str] = None
    EnabledUser: Optional[str] = None
    Grades: Optional[List[str]] = None
    FamilyKey: Optional[List[str]] = None
    SectionsIDs: Optional[str] = None
    GradebookIDs: Optional[List[str]] = None
    DateLastModified: Optional[str] = None
    school_code: Optional[str]  # Add the new field for SchoolCode

    class Config:
        from_attributes = True

class StudentInDBCreate(BaseModel):
    AnonymizedStudentID: str
    AnonymizedStudentNumber: Optional[str] = None
    role: RoleEnum

    class Config:
        from_attributes = True


class PeopleInDBResponse(PeopleInDBCreate):
    id: int

    class Config:
        from_attributes = True  
        

class StudentInDBResponse(StudentInDBCreate):
    id: int
    people: PeopleInDBResponse

    class Config:
        from_attributes = True

class SchoolsInDBBase(BaseModel):
    school_code: str
    school_name: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]

    class Config:
        orm_mode = True

class SchoolsInDBCreate(SchoolsInDBBase):
    pass

class SchoolsInDB(SchoolsInDBBase):
    id: int
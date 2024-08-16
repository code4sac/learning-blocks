
from typing import Optional, List
from pydantic import BaseModel
from models import RoleEnum 
        
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

class PeopleInDBResponse(PeopleInDBCreate):
    id: int

class StudentInDBCreate(BaseModel):
    anonymizedStudentID: str
    anonymizedStudentNumber: Optional[str] = None
    role: RoleEnum


class PeopleInDBResponse(PeopleInDBCreate):
    id: int

    class Config:
        from_attributes = True  
        

class StudentInDBResponse(StudentInDBCreate):
    id: int
    people: PeopleInDBResponse

    class Config:
        from_attributes = True
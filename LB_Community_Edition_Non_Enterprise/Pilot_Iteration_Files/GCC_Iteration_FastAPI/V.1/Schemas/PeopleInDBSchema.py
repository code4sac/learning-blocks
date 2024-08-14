from pydantic import BaseModel
from typing import List, Optional

class PeopleInDBSchema(BaseModel):
    AnonymizedStudentID: str
    AnonymizedStudentNumber: Optional[str] = None
    AnonymizedCounselorNumber: Optional[str] = None
    AnonymizedHomeroomTeacherNumber: Optional[str] = None
    GraduationCohort: Optional[str] = None
    SchoolCode: Optional[str] = None
    Birthdate: Optional[str] = None
    EnabledUser: Optional[str] = None
    Role: Optional[str] = None
    Identifier: Optional[str] = None
    Grades: Optional[List[str]] = None
    userIds: Optional[str] = None
    FamilyKey: Optional[List[str]] = None
    AssociatedAccounts: Optional[List[str]] = None
    SectionsIDs: Optional[List[str]] = None
    GradebookIDs: Optional[List[str]] = None
    DateLastModified: Optional[str] = None

    class Config:
        orm_mode = True

class PeopleInDBCreate(PeopleInDBSchema):
    pass

class PeopleInDB(PeopleInDBSchema):
    class Config:
        orm_mode = True

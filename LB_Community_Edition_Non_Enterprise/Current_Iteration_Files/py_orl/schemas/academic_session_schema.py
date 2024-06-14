from pydantic import BaseModel
from typing import List, Optional
from models.status import Status

class AcademicSessionBase(BaseModel):
    title: str
    startDate: str
    endDate: str
    type: str
    schoolYear: str
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    parentSourcedId: Optional[str] = None # Make parentSourcedId optional
    schoolSourcedId: str
    href: str
    metadata: Optional[dict] = {}

class AcademicSessionCreate(AcademicSessionBase):
    pass

class AcademicSessionUpdate(AcademicSessionBase):
    pass

class AcademicSessionInDBBase(AcademicSessionBase):
    class Config:
        from_attributes = True

class AcademicSession(AcademicSessionInDBBase):
    children: List['AcademicSession'] = []  # Recursive definition for children

class AcademicSessionInDB(AcademicSessionInDBBase):
    children: List['AcademicSessionInDB'] = []  # Recursive definition for children

from pydantic import BaseModel
from models.status import Status
from typing import List, Optional

class AcademicSessionBase(BaseModel):
    title: str
    startDate: str
    endDate: str
    type: str
    schoolYear: str
    sourcedId: str
    status: Status
    dateLastModified: str
    metadata: Optional[dict]
    parentSourcedId: Optional[str]  # Make parentSourcedId optional

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

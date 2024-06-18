from pydantic import BaseModel
from typing import Optional
from models.status import Status
from models.class_type import ClassType

class ClassBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    title: str
    grades: Optional[list] = []
    courseSourcedId: str
    classCode: Optional[str] = None
    classType: ClassType
    location: Optional[str] = None
    schoolSourcedId: str
    termSourcedIds: list
    subjects: Optional[list] = []
    subjectCodes: Optional[list] = []
    periods: Optional[list] = []

class ClassCreate(ClassBase):
    pass

class ClassUpdate(ClassBase):
    pass

class ClassInDBBase(ClassBase):
    class Config:
        from_orm = True  # Corrected attribute name

class Class(ClassInDBBase):
    pass

class ClassInDB(ClassInDBBase):
    pass

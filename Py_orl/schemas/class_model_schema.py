from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class ClassBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    title: str
    grades: str
    courseSourcedId: str
    classCode: str
    classType: Status
    location: str
    schoolSourcedId: str
    termSourcedIds: str
    subjects: str
    subjectCodes: str
    periods: str
    course: Optional[dict]  # Make it optional
    school: Optional[dict]  # Make it optional
    terms: Optional[list]  # Include this field
    classResources: Optional[list]  # Include this field
    enrollments: Optional[list]  # Include this field
    lineItems: Optional[list]  # Include this field

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

from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class EnrollmentBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    classSourcedId: str
    schoolSourcedId: str
    userSourcedId: str
    role: Status
    primary: Status
    beginDate: str
    endDate: str
    class_: Optional[str]  # Make class_ field optional using Optional from typing
    school: Optional[str]  # Make school field optional using Optional from typing
    user: Optional[str]  # Make user field optional using Optional from typing

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentUpdate(EnrollmentBase):
    pass

class EnrollmentInDBBase(EnrollmentBase):
    class Config:
        from_attributes  = True

class Enrollment(EnrollmentInDBBase):
    pass

class EnrollmentInDB(EnrollmentInDBBase):
    pass

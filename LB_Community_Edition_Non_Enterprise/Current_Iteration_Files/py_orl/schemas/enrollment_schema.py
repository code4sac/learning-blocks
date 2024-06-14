from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from models.role_type import RoleType
from models.true_false import TrueFalse

from typing import Optional

class EnrollmentBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    classSourcedId: str
    schoolSourcedId: str
    userSourcedId: str
    role: RoleType
    primary: Optional[TrueFalse] = None
    beginDate: Optional[str] = None
    endDate: Optional[str] = None

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

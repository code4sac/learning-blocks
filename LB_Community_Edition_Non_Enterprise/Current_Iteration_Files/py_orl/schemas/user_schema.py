from pydantic import BaseModel
from typing import Optional

from models.status import Status
from models.role_type import RoleType
from models.true_false import TrueFalse

class UserBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    enabledUser: TrueFalse
    role: RoleType
    username: str
    userIds: Optional[str] = None
    givenName: str
    familyName: str
    middleName: str = ""
    identifier: Optional[str] = None
    email: Optional[str] = None
    sms: Optional[str] = None
    phone: str = ""
    grades: Optional[str] = None
    password: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    class Config:
        from_attributes = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    pass

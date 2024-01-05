from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    sourcedId: str
    status: bool
    dateLastModified: str
    enabledUser: bool
    role: str
    username: str
    userIds: Optional[str] = None
    givenName: str
    familyName: str
    middleName: str = ""
    identifier: str
    email: str
    sms: Optional[str] = None
    phone: str = ""
    grades: Optional[str] = None
    password: Optional[str] = None
    orgs: Optional[list] = None
    agents: Optional[list] = None
    enrollments: Optional[list] = None
    results: Optional[list] = None

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

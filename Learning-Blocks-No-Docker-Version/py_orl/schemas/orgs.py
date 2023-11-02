from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class OrgsBase(BaseModel):
    sourcedId: str
    status: str
    dateLastModified: datetime
    name: str
    type: str
    identifier: Optional[str] = None
    parentSourcedId: str


class OrgsCreate(OrgsBase):
    sourcedId: str
    status: str
    dateLastModified: date
    name: str
    type: str
    identifier: Optional[str] = None
    parentSourcedId: str


class OrgsUpdate(OrgsBase):
    pass


class OrgsInDBBase(OrgsBase):
    sourcedId: str
    status: str
    dateLastModified: date
    name: str
    type: str
    identifier: Optional[str] = None

    class Config:
        from_attributes = True


class Orgs(OrgsInDBBase):
    pass


class OrgsInDB(OrgsInDBBase):
    pass

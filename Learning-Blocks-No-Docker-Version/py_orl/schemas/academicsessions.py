from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AcademicsessionsBase(BaseModel):
    sourcedId: int
    status: str
    dateLastModified: Optional[datetime] = None
    title: str
    type: str
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    parentSourcedId: str


class AcademicsessionsCreate(AcademicsessionsBase):
    sourcedId: int
    status: str
    dateLastModified: Optional[datetime] = None
    title: str
    type: str
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    parentSourcedId: str


class AcademicsessionsUpdate(AcademicsessionsBase):
    pass


class AcademicsessionsInDBBase(AcademicsessionsBase):
    sourcedId: int
    status: str
    dateLastModified: Optional[datetime] = None
    title: str
    type: str
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    parentSourcedId: str

    class Config:
        from_attributes = True


class Academicsessions(AcademicsessionsInDBBase):
    pass


class AcademicsessionsInDB(AcademicsessionsInDBBase):
    pass

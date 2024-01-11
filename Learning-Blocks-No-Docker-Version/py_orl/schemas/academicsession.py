from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AcademicsessionBase(BaseModel):
    sourcedId: int
    status: str
    dateLastModified: Optional[datetime] = None
    title: str
    type: str
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    parentSourcedId: str


class AcademicsessionCreate(AcademicsessionBase):
    sourcedId: int
    status: str
    dateLastModified: Optional[datetime] = None
    title: str
    type: str
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    parentSourcedId: str


class AcademicsessionUpdate(AcademicsessionBase):
    pass


class AcademicsessionInDBBase(AcademicsessionBase):
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


class Academicsession(AcademicsessionInDBBase):
    pass


class AcademicsessionInDB(AcademicsessionInDBBase):
    pass

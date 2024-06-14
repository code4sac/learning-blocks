from pydantic import BaseModel
from typing import Optional
from models.status import Status

class CourseResourceBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    title: str
    courseSourcedId: str
    resourceSourcedId: str

class CourseResourceCreate(CourseResourceBase):
    pass

class CourseResourceUpdate(CourseResourceBase):
    pass

class CourseResourceInDBBase(CourseResourceBase):
    class Config:
        from_attributes  = True

class CourseResource(CourseResourceInDBBase):
    pass

class CourseResourceInDB(CourseResourceInDBBase):
    pass

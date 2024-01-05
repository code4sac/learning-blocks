from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class CourseResourceBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    title: str
    courseSourcedId: str
    resourceSourcedId: str
    course: Optional[list] = None
    resource: Optional[list] = None

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

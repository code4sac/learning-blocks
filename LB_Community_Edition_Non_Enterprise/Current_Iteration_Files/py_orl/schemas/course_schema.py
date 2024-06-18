from pydantic import BaseModel
from typing import Optional
from models.status import Status  

class CourseBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    schoolYearSourcedId: Optional[str] = None
    title: str
    courseCode: Optional[str] = None
    grades: Optional[list] = []
    orgSourcedId: str
    subjects: Optional[list] = []
    subjectCodes: Optional[list] = []

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass

class CourseInDBBase(CourseBase):
    class Config:
        from_attributes  = True

class Course(CourseInDBBase):
    pass

class CourseInDB(CourseInDBBase):
    pass

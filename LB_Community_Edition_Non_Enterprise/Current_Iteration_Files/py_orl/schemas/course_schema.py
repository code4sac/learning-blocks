from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class CourseBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    schoolYearSourcedId: str
    title: str
    courseCode: str
    grades: str
    orgSourcedId: str
    subjects: str
    subjectCodes: str
    schoolYear: Optional[list] = None
    org: Optional[list] = None
    classes: Optional[list] = None
    courseResources: Optional[list] = None

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

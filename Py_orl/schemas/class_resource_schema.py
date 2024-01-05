from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class ClassResourceBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    title: str
    classSourcedId: str
    resourceSourcedId: str
    class_: Optional[list]
    resource: Optional[list] = None

class ClassResourceCreate(ClassResourceBase):
    pass

class ClassResourceUpdate(ClassResourceBase):
    pass

class ClassResourceInDBBase(ClassResourceBase):
    class Config:
        from_attributes  = True

class ClassResource(ClassResourceInDBBase):
    pass

class ClassResourceInDB(ClassResourceInDBBase):
    pass

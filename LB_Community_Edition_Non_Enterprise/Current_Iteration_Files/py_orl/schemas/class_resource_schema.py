from pydantic import BaseModel
from typing import Optional
from models.status import Status

class ClassResourceBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    title: str
    classSourcedId: str
    resourceSourcedId: str

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

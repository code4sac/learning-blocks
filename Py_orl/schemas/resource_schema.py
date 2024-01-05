from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class ResourceBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    vendorResourceId: str
    title: str
    roles: Status
    importance: Status
    vendorId: str
    applicationId: str
    classResources: Optional[str]
    courseResources: Optional[str]

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(ResourceBase):
    pass

class ResourceInDBBase(ResourceBase):
    class Config:
        from_attributes  = True

class Resource(ResourceInDBBase):
    pass

class ResourceInDB(ResourceInDBBase):
    pass

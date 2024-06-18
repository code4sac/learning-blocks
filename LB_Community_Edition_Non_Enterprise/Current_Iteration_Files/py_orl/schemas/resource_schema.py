from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from models.role_type import RoleType  # Adjust this import based on your dependencies
from models.importance import Importance  # Adjust this import based on your dependencies
from typing import Optional

class ResourceBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    vendorResourceId: str
    title: str
    roles: Optional[list[RoleType]] = []
    importance: Optional[Importance] = None
    vendorId: Optional[str] = None
    applicationId: Optional[str] = None

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

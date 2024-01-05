from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class CategoryBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    title: str
    metadata: Optional[dict]
    lineItems: Optional[str]

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryInDBBase(CategoryBase):
    class Config:
        from_attributes  = True

class Category(CategoryInDBBase):
    pass

class CategoryInDB(CategoryInDBBase):
    pass

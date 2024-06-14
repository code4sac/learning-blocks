from pydantic import BaseModel
from typing import Optional
from models.status import Status

class CategoryBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    title: str
    metadata: Optional[dict] = {}

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

from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class LineItemBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    title: str
    description: Optional[str] = None
    assignDate: str
    dueDate: str
    classSourcedId: str
    categorySourcedId: str
    gradingPeriodSourcedId: str
    resultValueMin: float
    resultValueMax: float
    metadata: Optional[dict] = {}

class LineItemCreate(LineItemBase):
    pass

class LineItemUpdate(LineItemBase):
    pass

class LineItemInDBBase(LineItemBase):
    class Config:
        from_attributes  = True

class LineItem(LineItemInDBBase):
    pass

class LineItemInDB(LineItemInDBBase):
    pass

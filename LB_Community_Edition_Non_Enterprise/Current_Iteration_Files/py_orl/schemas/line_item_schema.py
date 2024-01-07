from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class LineItemBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    title: str
    description: str
    assignDate: str
    dueDate: str
    classSourcedId: str
    categorySourcedId: str
    gradingPeriodSourcedId: str
    resultValueMin: str
    resultValueMax: str
    class_: Optional[list] = None
    category: Optional[list] = None
    gradingPeriod: Optional[list] = None
    results: Optional[list] = None

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

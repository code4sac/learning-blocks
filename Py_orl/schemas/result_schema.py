from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from typing import Optional

class ResultBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    lineItemSourcedId: str
    studentSourcedId: str
    scoreStatus: Status
    score: str
    scoreDate: str
    comment: str
    lineItem: Optional[list]
    student: Optional[list]

class ResultCreate(ResultBase):
    pass

class ResultUpdate(ResultBase):
    pass

class ResultInDBBase(ResultBase):
    class Config:
        from_attributes  = True

class Result(ResultInDBBase):
    pass

class ResultInDB(ResultInDBBase):
    pass

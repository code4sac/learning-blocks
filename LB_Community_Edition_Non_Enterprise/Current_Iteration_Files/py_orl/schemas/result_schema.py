from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies
from models.score_status import ScoreStatus

from typing import Optional

class ResultBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    lineItemSourcedId: str
    studentSourcedId: str
    scoreStatus: ScoreStatus
    score: str
    scoreDate: str
    comment: Optional[str] = None

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

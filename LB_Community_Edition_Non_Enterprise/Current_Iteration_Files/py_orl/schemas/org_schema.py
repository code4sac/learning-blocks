from pydantic import BaseModel
from typing import List, Optional

from models.status import Status

class OrgChild(BaseModel):
    href: str
    sourcedId: str
    type: str

class OrgBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    name: str
    type: str
    identifier: Optional[str] = None
    parentSourcedId: Optional[str] = None
    # children: List[OrgChild] = [] # org currently does not have children in the model
    # Define other relationships as needed

class OrgCreate(OrgBase):
    pass

class OrgUpdate(OrgBase):
    pass

class OrgInDBBase(OrgBase):
    class Config:
        from_attributes = True

class Org(OrgInDBBase):
    pass

class OrgInDB(OrgInDBBase):
    pass

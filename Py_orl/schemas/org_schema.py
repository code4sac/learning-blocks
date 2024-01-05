from pydantic import BaseModel
from typing import List, Optional

class OrgChild(BaseModel):
    href: str
    sourcedId: str
    type: str

class OrgBase(BaseModel):
    sourcedId: str
    status: str
    dateLastModified: str
    name: str
    type: str
    identifier: Optional[str] = None
    parentSourcedId: Optional[str] = None
    children: List[OrgChild] = []
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

from pydantic import BaseModel
from typing import List, Optional

class UserAssociationSchema(BaseModel):
    id: int
    family_key: Optional[List[str]] = None
    associated_accounts: Optional[List[str]] = None
    people_id: Optional[str] = None

    class Config:
        orm_mode = True

class UserAssociationCreate(UserAssociationSchema):
    pass

class UserAssociationUpdate(UserAssociationSchema):
    pass

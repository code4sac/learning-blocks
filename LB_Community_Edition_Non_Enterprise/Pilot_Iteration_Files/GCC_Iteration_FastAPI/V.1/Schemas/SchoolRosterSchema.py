from pydantic import BaseModel
from typing import Optional

class SchoolRosterSchema(BaseModel):
    id: int
    school_code: Optional[str] = None
    people_id: Optional[str] = None

    class Config:
        orm_mode = True

class SchoolRosterCreate(SchoolRosterSchema):
    pass

class SchoolRosterUpdate(SchoolRosterSchema):
    pass

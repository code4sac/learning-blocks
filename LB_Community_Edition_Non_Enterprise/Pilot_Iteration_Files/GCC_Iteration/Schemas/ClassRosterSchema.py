from pydantic import BaseModel
from typing import List, Optional

class ClassRosterSchema(BaseModel):
    id: int
    sections_ids: Optional[List[str]] = None
    people_id: Optional[str] = None

    class Config:
        orm_mode = True

class ClassRosterCreate(ClassRosterSchema):
    pass

class ClassRosterUpdate(ClassRosterSchema):
    pass

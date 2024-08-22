from pydantic import BaseModel
from typing import List, Optional

class GradebookAssociationSchema(BaseModel):
    id: int
    gradebook_ids: Optional[List[str]] = None
    people_id: Optional[str] = None

    class Config:
        orm_mode = True

class GradebookAssociationCreate(GradebookAssociationSchema):
    pass

class GradebookAssociationUpdate(GradebookAssociationSchema):
    pass

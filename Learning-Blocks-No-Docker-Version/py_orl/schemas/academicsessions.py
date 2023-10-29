from pydantic import BaseModel


class academicsessionsBase(BaseModel):
    sourceId: int
    name: str


class academicsessionsCreate(academicsessionsBase):
    sourceId: int
    name: str


class academicsessionsUpdate(academicsessionsBase):
    pass


class academicsessionsInDBBase(academicsessionsBase):
    sourceId: int
    name: str

    class Config:
        from_attributes = True


class Org(academicsessionsInDBBase):
    pass


class OrgInDB(academicsessionsInDBBase):
    pass

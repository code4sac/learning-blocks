from pydantic import BaseModel


class OrgBase(BaseModel):
    sourceId: int
    name: str


class OrgCreate(OrgBase):
    sourceId: int
    name: str


class OrgUpdate(OrgBase):
    pass


class OrgInDBBase(OrgBase):
    id: int
    sourceId: int
    name: str

    class Config:
        from_attributes = True


class Org(OrgInDBBase):
    pass


class OrgInDB(OrgInDBBase):
    pass

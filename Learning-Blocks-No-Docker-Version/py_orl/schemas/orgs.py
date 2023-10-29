from pydantic import BaseModel


class OrgBase(BaseModel):
    sourceId: int
    title: str


class OrgCreate(OrgBase):
    sourceId: int
    title: str


class OrgUpdate(OrgBase):
    pass


class OrgInDBBase(OrgBase):
    sourceId: int
    title: str

    class Config:
        from_attributes = True


class Org(OrgInDBBase):
    pass


class OrgInDB(OrgInDBBase):
    pass

from pydantic import BaseModel


class OrgBase(BaseModel):
    name: str


class OrgCreate(OrgBase):
    name: str


class OrgUpdate(OrgBase):
    pass


class OrgInDBBase(OrgBase):
    sourceId: str
    name: str

    class Config:
        from_attributes = True


class Org(OrgInDBBase):
    pass


class OrgInDB(OrgInDBBase):
    pass

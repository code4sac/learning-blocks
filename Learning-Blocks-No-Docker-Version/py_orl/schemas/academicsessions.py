from pydantic import BaseModel


class AcademicsessionsBase(BaseModel):
    sourcedId: int
    name: str


class AcademicsessionsCreate(AcademicsessionsBase):
    sourcedId: int
    name: str


class AcademicsessionsUpdate(AcademicsessionsBase):
    pass


class AcademicsessionsInDBBase(AcademicsessionsBase):
    sourcedId: int
    name: str

    class Config:
        from_attributes = True


class Org(AcademicsessionsInDBBase):
    pass


class OrgInDB(AcademicsessionsInDBBase):
    pass

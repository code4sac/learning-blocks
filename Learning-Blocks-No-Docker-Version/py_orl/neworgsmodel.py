from typing import Union, Optional
from sqlmodel import Field, Relationship, SQLModel
from models.status import Status
from models.org_type import OrgType
import pydantic


# Shared properties
class OrgBase(SQLModel):
    sourcedId: str
    status: Optional[str]
    dateLastModified: Optional[str]
    name: str
    type: str
    identifier: Optional[str]
    parentSourcedId: Optional[str] = Field(default=None, foreign_key="org.sourcedId")


# Properties to receive on item creation
class OrgCreate(OrgBase):
    sourcedId: str
    name: str
    type: str


# Properties to receive on item update
class OrgUpdate(OrgBase):
    status: Optional[str]
    dateLastModified: Optional[str]
    name: str
    type: str
    identifier: Optional[str]
    parentSourcedId: Optional[str] = Field(default=None,foreign_key="org.sourcedId")


# Database model, database table inferred from class name
class Org(OrgBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sourcedId: str
    name: str
    type: str
    # title: str
    # owner_id: Union[int, None] = Field(
    #     default=None, foreign_key="user.id", nullable=False
    # )
    # owner: Union[User, None] = Relationship(back_populates="items")


# Properties to return via API, id is always required
class OrgOut(OrgBase):
    pass  
    # id: int





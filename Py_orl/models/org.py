from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum, Boolean, UUID
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.org_type import OrgType
from models.status import Status


class Orgs(Base):
    __tablename__ = "org"

    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    name = Column(String(255), nullable=False)
    type = Column(Enum(OrgType), nullable=False)
    identifier = Column(String(255), nullable=True)
    parentSourcedId = Column(UUID(), ForeignKey("org.sourcedId"), nullable=True)

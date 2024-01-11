from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, UUID

from db.base_class import Base
from models.status import Status


class ClassResource(Base):
    __tablename__ = "class_resource"

    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    title = Column(String(255), nullable=True)
    classSourcedId = Column(UUID(), ForeignKey('class.sourcedId'), nullable=False)
    resourceSourcedId = Column(UUID(), ForeignKey('resource.sourcedId'), nullable=False)

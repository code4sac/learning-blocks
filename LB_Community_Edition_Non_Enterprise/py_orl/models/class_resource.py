from sqlalchemy import Column, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from db.base_class import Base
from models.status import Status


class ClassResource(Base):
    __tablename__ = "class_resource"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    title = Column(String(255), nullable=True)
    classSourcedId = Column(String(255), ForeignKey('class.sourcedId'), nullable=False)
    resourceSourcedId = Column(String(255), ForeignKey('resource.sourcedId'), nullable=False)

    class_ = relationship('Class', back_populates='classResources')
    resource = relationship('Resource', back_populates='classResources')

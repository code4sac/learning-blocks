from sqlalchemy import Column, String, DateTime, Enum, ARRAY, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base
from models.importance import Importance
from models.role_type import RoleType
from models.status import Status


class Resource(Base):
    """
    Resources dataset for OneRoster 3.12 specification.
    """
    __tablename__ = "resource"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime(), nullable=True)
    vendorResourceId = Column(String(255), unique=True, nullable=False)
    title = Column(String(255), nullable=True)
    roles = Column(ARRAY(Enum(RoleType)), nullable=True)
    importance = Column(Enum(Importance), nullable=True)
    vendorId = Column(String(255), nullable=True)
    applicationId = Column(String(255), nullable=True)

    classResources = relationship('ClassResource', back_populates='resource')
    courseResources = relationship('CourseResource', back_populates='resource')
    # Metadata column
    custom_metadata = Column('metadata', JSON, nullable=True)

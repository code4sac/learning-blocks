from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.status import Status


class CourseResource(Base):
    """
    Course resources association model based on OneRoster 3.6 specification.
    """
    __tablename__ = "course_resource"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)  # Nullable for Bulk mode
    dateLastModified = Column(DateTime, nullable=True)  # Nullable for Bulk mode
    title = Column(String(255), nullable=True)
    courseSourcedId = Column(String(255), ForeignKey('course.sourcedId'), nullable=False)
    resourceSourcedId = Column(String(255), ForeignKey('resource.sourcedId'), nullable=False)

    course = relationship('Course', back_populates='courseResources')
    resource = relationship('Resource', back_populates='courseResources')
    # Metadata column
    custom_metadata = Column('metadata', JSON, nullable=True)

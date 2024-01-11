from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, UUID

from db.base_class import Base
from models.status import Status


class CourseResource(Base):
    """
    Course resources association model based on OneRoster 3.6 specification.
    """
    __tablename__ = "course_resource"

    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)  # Nullable for Bulk mode
    dateLastModified = Column(DateTime, nullable=True)  # Nullable for Bulk mode
    title = Column(String(255), nullable=True)
    courseSourcedId = Column(UUID(), ForeignKey('course.sourcedId'), nullable=False)
    resourceSourcedId = Column(UUID(), ForeignKey('resource.sourcedId'), nullable=False)

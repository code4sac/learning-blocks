from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, UUID, ARRAY

from db.base_class import Base
from models.status import Status


class Course(Base):
    """
    Course model based on OneRoster 3.7 specification.
    """
    __tablename__ = "course"

    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)  # Nullable for Bulk mode
    dateLastModified = Column(DateTime, nullable=True)  # Nullable for Bulk mode
    schoolYearSourcedId = Column(UUID(), ForeignKey('academic_session.sourcedId'), nullable=True)
    title = Column(String(255), nullable=False)
    courseCode = Column(String(255), nullable=True)
    grades = Column(ARRAY(String(255)), nullable=True)  # String type can store a comma-separated list of grades
    orgSourcedId = Column(UUID(), ForeignKey('org.sourcedId'), nullable=False)
    subjects = Column(ARRAY(String(255)), nullable=True)  # String type can store a comma-separated list of subjects
    subjectCodes = Column(ARRAY(String(255)), nullable=True)  # String type for subject codes

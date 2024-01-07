from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.status import Status


class Course(Base):
    """
    Course model based on OneRoster 3.7 specification.
    """
    __tablename__ = "course"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)  # Nullable for Bulk mode
    dateLastModified = Column(DateTime, nullable=True)  # Nullable for Bulk mode
    schoolYearSourcedId = Column(String(255), ForeignKey('academic_session.sourcedId'), nullable=True)
    title = Column(String(255), nullable=False)
    courseCode = Column(String(255), nullable=True)
    grades = Column(ARRAY(String(255)), nullable=True)  # String type can store a comma-separated list of grades
    orgSourcedId = Column(String(255), ForeignKey('org.sourcedId'), nullable=False)
    subjects = Column(ARRAY(String(255)), nullable=True)  # String type can store a comma-separated list of subjects
    subjectCodes = Column(ARRAY(String(255)), nullable=True)  # String type for subject codes

    schoolYear = relationship("AcademicSession", back_populates='courses')
    org = relationship("Org", back_populates="courses")
    classes = relationship('Class', back_populates='course')
    courseResources = relationship('CourseResource', back_populates='course')

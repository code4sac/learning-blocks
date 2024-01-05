from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, Text, Table, UUID, ARRAY
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.class_type import ClassType
from models.status import Status


class Class(Base):
    """
    Class model with dependencies based on OneRoster 3.4 specification.
    """
    __tablename__ = "class"

    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    title = Column(String(255), nullable=False)
    grades = Column(ARRAY(String(255)), nullable=True)
    courseSourcedId = Column(UUID(), ForeignKey('course.sourcedId'), nullable=False)
    classCode = Column(String(255), nullable=True)
    classType = Column(Enum(ClassType), nullable=False)
    location = Column(String(255), nullable=True)
    schoolSourcedId = Column(UUID(), ForeignKey('org.sourcedId'), nullable=False)
    termSourcedIds = Column(ARRAY(UUID()), nullable=False)
    subjects = Column(ARRAY(String(255)), nullable=True)
    subjectCodes = Column(ARRAY(String(255)), nullable=True)
    periods = Column(ARRAY(String(255)), nullable=True)

from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.class_term import class_term
from models.class_type import ClassType
from models.status import Status


class Class(Base):
    """
    Class model with dependencies based on OneRoster 3.4 specification.
    """
    __tablename__ = "class"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    title = Column(String(255), nullable=False)
    grades = Column(ARRAY(String(255)), nullable=True)
    courseSourcedId = Column(String(255), ForeignKey('course.sourcedId'), nullable=False)
    classCode = Column(String(255), nullable=True)
    classType = Column(Enum(ClassType), nullable=False)
    location = Column(String(255), nullable=True)
    schoolSourcedId = Column(String(255), ForeignKey('org.sourcedId'), nullable=False)
    termSourcedIds = Column(ARRAY(String(255)), nullable=False)
    subjects = Column(ARRAY(String(255)), nullable=True)
    subjectCodes = Column(ARRAY(String(255)), nullable=True)
    periods = Column(ARRAY(String(255)), nullable=True)

    course = relationship('Course', back_populates='classes')
    school = relationship('Org', back_populates='classes')
    terms = relationship("AcademicSession", secondary=class_term, back_populates="classes")
    classResources = relationship('ClassResource', back_populates='class_')
    enrollments = relationship("Enrollment", back_populates="class_")
    lineItems = relationship("LineItem", back_populates="class_")

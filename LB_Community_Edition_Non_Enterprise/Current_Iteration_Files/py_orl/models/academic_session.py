from sqlalchemy import Column, String, Enum, DateTime, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.class_term import class_term
from models.status import Status

class AcademicSession(Base):
    """
    Academic session model based on OneRoster 3.2 specification.
    """
    __tablename__ = "academic_session"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    title = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)  # You can adjust the length as needed
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    parentSourcedId = Column(String(255), ForeignKey('academic_session.sourcedId'), nullable=True)
    schoolYear = Column(Integer, nullable=False)
    schoolSourcedId = Column(String(255), ForeignKey('org.sourcedId'), nullable=False)

    href = Column(String(255), nullable=False)

    # Parent and Children relationships with href, sourcedId, and type
    parent = relationship(
        "AcademicSession",
        remote_side=[sourcedId],
        back_populates="children",
        foreign_keys=[parentSourcedId],
    )
    children = relationship(
        "AcademicSession",
        back_populates="parent",
        cascade="all, delete-orphan",
        foreign_keys=[parentSourcedId],
    )

    school = relationship("Org", back_populates="schools")
    classes = relationship("Class", secondary=class_term, back_populates="terms")
    courses = relationship("Course", back_populates='schoolYear')
    lineItems = relationship("LineItem", back_populates="gradingPeriod")

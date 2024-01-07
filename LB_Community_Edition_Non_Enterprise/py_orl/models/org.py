from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.org_type import OrgType
from models.status import Status


class Org(Base):
    __tablename__ = "org"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    name = Column(String(255), nullable=False)
    type = Column(Enum(OrgType), nullable=False)
    identifier = Column(String(255), nullable=True)
    parentSourcedId = Column(String(255), ForeignKey("org.sourcedId"), nullable=True)

    parent = relationship("Org", remote_side=[sourcedId])
    schools = relationship("AcademicSession", back_populates="school")
    classes = relationship('Class', back_populates='school')
    courses = relationship("Course", back_populates="org")
    enrollments = relationship("Enrollment", back_populates="school")
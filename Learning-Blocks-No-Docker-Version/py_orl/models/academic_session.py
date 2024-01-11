from sqlalchemy import Column, String, Enum, DateTime, Date, Integer, ForeignKey, UUID

from db.base_class import Base
from models.session_type import SessionType
from models.status import Status


class AcademicSession(Base):
    """
    Academic session model based on OneRoster 3.2 specification.
    """
    __tablename__ = "academic_session"

    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    title = Column(String(255), nullable=False)
    type = Column(Enum(SessionType), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    parentSourcedId = Column(UUID(), ForeignKey('academic_session.sourcedId'), nullable=True)
    schoolYear = Column(Integer, nullable=False)
    schoolSourcedId = Column(UUID(), ForeignKey('org.sourcedId'),
                             nullable=False)  # New attribute for school reference

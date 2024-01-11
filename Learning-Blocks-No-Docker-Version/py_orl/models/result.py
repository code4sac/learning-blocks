from sqlalchemy import Column, String, Float, DateTime, Enum, ForeignKey, UUID, Date

from db.base_class import Base
from models.score_status import ScoreStatus
from models.status import Status


class Result(Base):
    """
    Results dataset for OneRoster 3.13 specification.
    """
    __tablename__ = "result"

    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime(), nullable=True)
    lineItemSourcedId = Column(UUID(), ForeignKey('line_item.sourcedId'), nullable=False)
    studentSourcedId = Column(UUID(), ForeignKey('user.sourcedId'), nullable=False)
    scoreStatus = Column(Enum(ScoreStatus), nullable=False)
    score = Column(Float, nullable=False)
    scoreDate = Column(Date, nullable=False)
    comment = Column(String(255), nullable=True)

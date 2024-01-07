from sqlalchemy import Column, String, Float, DateTime, Enum, ForeignKey, Date, JSON
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.score_status import ScoreStatus
from models.status import Status


class Result(Base):
    """
    Results dataset for OneRoster 3.13 specification.
    """
    __tablename__ = "result"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime(), nullable=True)
    lineItemSourcedId = Column(String(255), ForeignKey('line_item.sourcedId'), nullable=False)
    studentSourcedId = Column(String(255), ForeignKey('user.sourcedId'), nullable=False)
    scoreStatus = Column(Enum(ScoreStatus), nullable=False)
    score = Column(Float, nullable=False)
    scoreDate = Column(Date, nullable=False)
    comment = Column(String(255), nullable=True)

    lineItem = relationship("LineItem", back_populates="results")
    student = relationship("User", back_populates="results")
    # Metadata column
    custom_metadata = Column('metadata', JSON, nullable=True)

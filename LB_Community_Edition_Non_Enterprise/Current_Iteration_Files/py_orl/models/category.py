from sqlalchemy import Column, String, Enum, DateTime, JSON
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.status import Status


class Category(Base):
    """
    Line Item Categories model based on OneRoster 3.3 specification.
    """
    __tablename__ = "category"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    title = Column(String(255), nullable=False)



    lineItems = relationship("LineItem", back_populates="category")

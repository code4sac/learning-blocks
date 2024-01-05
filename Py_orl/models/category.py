from sqlalchemy import Column, String, Enum, DateTime, UUID
from db.base_class import Base
from models.status import Status


class Category(Base):
    """
    Line Item Categories model based on OneRoster 3.3 specification.
    """
    __tablename__ = "category"

    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)  # Nullable for Bulk mode
    dateLastModified = Column(DateTime, nullable=True)  # Nullable for Bulk mode
    title = Column(String(255), nullable=False)  # Specify length for consistency

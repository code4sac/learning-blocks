from sqlalchemy import Column, String, Enum, DateTime, Date, Float, ForeignKey, UUID

from db.base_class import Base
from models.status import Status


class LineItem(Base):
    """
    LineItem data model for OneRoster 3.10 specification.
    """
    __tablename__ = "line_item"

    # Unique identifier for each line item
    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)

    # LineItem status
    status = Column(Enum(Status), nullable=True)  # Nullable for Bulk mode

    # Date of last modification
    dateLastModified = Column(DateTime, nullable=True)  # Nullable for Bulk mode

    # Title of the line item
    title = Column(String(255), nullable=False)

    # Description of the line item
    description = Column(String(255), nullable=True)

    # Date the associated activity was assigned
    assignDate = Column(Date, nullable=False)

    # Due date for the line item
    dueDate = Column(Date, nullable=False)

    # SourcedId of the Class
    classSourcedId = Column(UUID(), ForeignKey('class.sourcedId'), nullable=False)

    # SourcedId of the Category
    categorySourcedId = Column(UUID(), ForeignKey('category.sourcedId'), nullable=False)

    # SourcedId of the academic session defining the grading period
    gradingPeriodSourcedId = Column(UUID(), ForeignKey('academic_session.sourcedId'), nullable=False)

    # Minimum and maximum values for the score
    resultValueMin = Column(Float, nullable=False)
    resultValueMax = Column(Float, nullable=False)

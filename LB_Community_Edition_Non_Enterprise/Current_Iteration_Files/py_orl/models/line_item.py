from sqlalchemy import Column, String, Enum, DateTime, Date, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.status import Status


class LineItem(Base):
    """
    LineItem data model for OneRoster 3.10 specification.
    """
    __tablename__ = "line_item"

    # Unique identifier for each line item
    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)

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
    classSourcedId = Column(String(255), ForeignKey('class.sourcedId'), nullable=False)

    # SourcedId of the Category
    categorySourcedId = Column(String(255), ForeignKey('category.sourcedId'), nullable=False)

    # SourcedId of the academic session defining the grading period
    gradingPeriodSourcedId = Column(String(255), ForeignKey('academic_session.sourcedId'), nullable=False)

    # Minimum and maximum values for the score
    resultValueMin = Column(Float, nullable=False)
    resultValueMax = Column(Float, nullable=False)

    class_ = relationship("Class", back_populates="lineItems")
    category = relationship("Category", back_populates="lineItems")
    gradingPeriod = relationship("AcademicSession", back_populates="lineItems")
    results = relationship("Result", back_populates="lineItem")
    # Metadata column
    custom_metadata = Column('metadata', JSON, nullable=True)

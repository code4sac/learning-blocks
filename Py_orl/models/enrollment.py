from sqlalchemy import Column, String, Enum, DateTime, Boolean, Date, ForeignKey, UUID
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.role_type import RoleType
from models.status import Status
from models.true_false import TrueFalse


class Enrollment(Base):
    """
    Enrollment data model for OneRoster 3.9 specification.
    """
    __tablename__ = "enrollment"

    # Unique identifier for each enrollment record
    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)

    # Enrollment status
    status = Column(Enum(Status), nullable=True)  # Nullable for Bulk mode

    # Date of last modification
    dateLastModified = Column(DateTime, nullable=True)  # Nullable for Bulk mode

    # SourcedId of the Class
    classSourcedId = Column(UUID(), ForeignKey('class.sourcedId'), nullable=False)

    # SourcedId of the School
    schoolSourcedId = Column(UUID(), ForeignKey('org.sourcedId'), nullable=False)

    # SourcedId of the User
    userSourcedId = Column(UUID(), ForeignKey('user.sourcedId'), nullable=False)

    # Role of the user in the class
    role = Column(Enum(RoleType), nullable=False)

    # Indicates if the teacher is the primary teacher for the class
    primary = Column(Enum(TrueFalse), nullable=True)  # Applicable only to teachers

    # Start date of the enrollment
    beginDate = Column(Date, nullable=True)

    # End date of the enrollment
    endDate = Column(Date, nullable=True)

    # Relationships with Class, School, and User models (if they exist)
    class_ = relationship("Class", back_populates="class_enrollments")
    school = relationship("School", back_populates="school_enrollments")
    user = relationship("User", back_populates="user_enrollments")

    # Add additional fields or modify as per your database schema

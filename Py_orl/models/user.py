from sqlalchemy import Column, String, Enum, DateTime, ARRAY, UUID
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.role_type import RoleType
from models.status import Status
from models.true_false import TrueFalse


class User(Base):
    """
    User model based on OneRoster 3.14 specification.
    """
    __tablename__ = "user"

    sourcedId = Column(UUID(), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    enabledUser = Column(Enum(TrueFalse), nullable=False)
    orgSourcedIds = Column(ARRAY(UUID()), nullable=False)
    role = Column(Enum(RoleType), nullable=False)
    username = Column(String(255), nullable=False)
    userIds = Column(ARRAY(String(255)), nullable=True)
    givenName = Column(String(255), nullable=False)
    familyName = Column(String(255), nullable=False)
    middleName = Column(String(255), nullable=True)
    identifier = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    sms = Column(String(255), nullable=True)
    phone = Column(String(255), nullable=True)
    agentSourcedIds = Column(ARRAY(UUID()), nullable=True)
    grades = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)

from sqlalchemy import Column, String, Enum, DateTime, ARRAY, Table, ForeignKey, JSON
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.role_type import RoleType
from models.status import Status
from models.true_false import TrueFalse
from models.user_agent import user_agent
from models.user_org import user_org


class User(Base):
    """
    User model based on OneRoster 3.14 specification.
    """
    __tablename__ = "user"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    enabledUser = Column(Enum(TrueFalse), nullable=False)
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
    grades = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)

    orgs = relationship("Org", secondary=user_org, back_populates="users")
    agents = relationship("User", secondary=user_agent, back_populates="users")
    enrollments = relationship("Enrollment", back_populates="user")
    results = relationship("Result", back_populates="student")
    # Metadata column
    custom_metadata = Column('metadata', JSON, nullable=True)

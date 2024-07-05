from sqlalchemy import Column, String, ARRAY, ForeignKey, Integer, Enum, Float, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Optional

Base = declarative_base()

# Define the enumeration for Role
class RoleEnum(str, Enum):
    administrator = "administrator"
    aide = "aide"
    guardian = "guardian"
    parent = "parent"
    proctor = "proctor"
    relative = "relative"
    student = "student"
    teacher = "teacher"

class PeopleInDB(Base):
    __tablename__ = "people_in_db"

    AnonymizedStudentID: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    AnonymizedStudentNumber: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    AnonymizedCounselorNumber: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    AnonymizedHomeroomTeacherNumber: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    GraduationCohort: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    SchoolCode: Mapped[Optional[str]] = mapped_column(String, ForeignKey('schools.school_code'), index=True, default=None)
    Birthdate: Mapped[Optional[str]] = mapped_column(String, default=None)
    EnabledUser: Mapped[Optional[str]] = mapped_column(String, default=None)
    Role: Column[RoleEnum] = Column(String(length=50))  # Use RoleEnum as the type for Role
    Identifier: Mapped[Optional[str]] = mapped_column(String, ForeignKey('different_users.Identifier'), default=None)
    Grades: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), default=None)
    userIds: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    FamilyKey: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), default=None)
    SectionsIDs: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), default=None)
    GradebookIDs: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), default=None)
    DateLastModified: Mapped[Optional[str]] = mapped_column(String, default=None)
    
    # Relationships
    schools: Mapped['SchoolRoster'] = relationship("SchoolRoster", back_populates="people")
    AssociatedAccounts: Mapped[List['UserAssociation']] = relationship("UserAssociation", back_populates="people")
    different_classes: Mapped[List['ClassRoster']] = relationship("ClassRoster", back_populates="people")
    different_gradebooks: Mapped[List['GradebookAssociation']] = relationship("GradebookAssociation", back_populates="people")

    # Relationship to Student table based on Role
    @property
    def student_info(self) -> Optional['Student']:
        if self.Role == RoleEnum.student:
            return self._student_info
        return None

    @student_info.setter
    def student_info(self, student: 'Student') -> None:
        if self.Role == RoleEnum.student:
            self._student_info = student

class Student(Base):
    __tablename__ = "student"

    AnonymizedStudentID: Mapped[str] = mapped_column(String, ForeignKey('people_in_db.AnonymizedStudentID'), primary_key=True, index=True)
    GradeLevel: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    GPA: Mapped[Optional[float]] = mapped_column(Float, index=True, default=None)
    HonorRoll: Mapped[Optional[bool]] = mapped_column(Boolean, index=True, default=None)
    Absences: Mapped[Optional[int]] = mapped_column(Integer, index=True, default=None)
    
    # Relationship to PeopleInDB
    person: Mapped['PeopleInDB'] = relationship('PeopleInDB', back_populates='student_info')

class SchoolRoster(Base):
    __tablename__ = "schools"

    SchoolRosterID: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    school_code: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    name: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)

    # Relationships
    people: Mapped[List['PeopleInDB']] = relationship("PeopleInDB", back_populates="schools")

class UserAssociation(Base):
    __tablename__ = "different_users"

    UserAssociationID: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    Identifier: Mapped[str] = mapped_column(String, ForeignKey('people_in_db.Identifier'), primary_key=True, index=True)
    FamilyKey: Mapped[str] = mapped_column(String, ForeignKey('people_in_db.FamilyKey'), index=True)
    
    # Relationships
    AssociatedAccounts: Mapped['PeopleInDB'] = relationship("PeopleInDB", back_populates="AssociatedAccounts")

class ClassRoster(Base):
    __tablename__ = "different_classes"

    ClassRosterID: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    Identifier: Mapped[str] = mapped_column(String, ForeignKey('people_in_db.Identifier'), primary_key=True, index=True)
    SectionsIDs: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), ForeignKey('people_in_db.SectionsIDs'), index=True, default=None)

    # Relationships
    people: Mapped['PeopleInDB'] = relationship("PeopleInDB", back_populates="different_classes")

class GradebookAssociation(Base):
    __tablename__ = "different_gradebooks"

    GradebookAssociationID: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    Identifier: Mapped[str] = mapped_column(String, ForeignKey('people_in_db.Identifier'), primary_key=True, index=True)
    GradebookIDs: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), ForeignKey('people_in_db.GradebookIDs'), index=True, default=None)

    # Relationships
    people: Mapped['PeopleInDB'] = relationship("PeopleInDB", back_populates="different_gradebooks")

class ChatSession(Base):
    __tablename__ = "chat_session"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    api_key: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    
    # Relationships
    messages: Mapped[List['Message']] = relationship("Message", back_populates="chat_session")

class Message(Base):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content: Mapped[str] = mapped_column(String)
    timestamp: Mapped[str] = mapped_column(String)

    # Foreign Key relationship
    chat_session_id: Mapped[int] = mapped_column(Integer, ForeignKey('chat_session.id'))

    # Relationships
    chat_session: Mapped['ChatSession'] = relationship("ChatSession", back_populates="messages")

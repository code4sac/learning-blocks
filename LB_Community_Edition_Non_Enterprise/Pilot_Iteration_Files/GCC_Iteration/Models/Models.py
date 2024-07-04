from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional, List

Base = declarative_base()

class PeopleInDB(Base):
    __tablename__ = "people_in_db"

    AnonymizedStudentID: str = Column(String, primary_key=True, index=True)
    AnonymizedStudentNumber: Optional[str] = Column(String, index=True, default=None)
    AnonymizedCounselorNumber: Optional[str] = Column(String, index=True, default=None)
    AnonymizedHomeroomTeacherNumber: Optional[str] = Column(String, index=True, default=None)
    GraduationCohort: Optional[str] = Column(String, index=True, default=None)
    SchoolCode: Optional[str] = Column(String, index=True, default=None)
    Birthdate: Optional[str] = Column(String, default=None)
    EnabledUser: Optional[str] = Column(String, default=None)
    Role: Optional[str] = Column(String, default=None)
    Identifier: Optional[str] = Column(String, default=None)
    Grades: Optional[List[str]] = Column(ARRAY(String), default=None)
    userIds: Optional[str] = Column(String, index=True, default=None)
    FamilyKey: Optional[List[str]] = Column(ARRAY(String), default=None)
    AssociatedAccounts: Optional[List[str]] = Column(ARRAY(String), default=None)
    SectionsIDs: Optional[List[str]] = Column(ARRAY(String), default=None)
    GradebookIDs: Optional[List[str]] = Column(ARRAY(String), default=None)
    DateLastModified: Optional[str] = Column(String, default=None)
    
    # Relationships using ForeignKey and back_populates
    schools: List["SchoolRoster"] = relationship("SchoolRoster", back_populates="people")
    different_users: List["UserAssociation"] = relationship("UserAssociation", back_populates="people")
    different_classes: List["ClassRoster"] = relationship("ClassRoster", back_populates="people")
    different_gradebooks: List["GradebookAssociation"] = relationship("GradebookAssociation", back_populates="people")

class SchoolRoster(Base):
    __tablename__ = "schools"

    id: int = Column(Integer, primary_key=True, index=True)
    school_code: Optional[str] = Column(String, index=True, default=None)
    people_id: Optional[str] = Column(String, ForeignKey('people_in_db.SchoolCode'), default=None)

    # Relationship to PeopleInDB using back_populates
    people: Optional[PeopleInDB] = relationship("PeopleInDB", back_populates="schools")

class UserAssociation(Base):
    __tablename__ = "different_users"

    id: int = Column(Integer, primary_key=True, index=True)
    family_key: Optional[List[str]] = Column(ARRAY(String), default=None)
    associated_accounts: Optional[List[str]] = Column(ARRAY(String), default=None)
    people_id: Optional[str] = Column(String, ForeignKey('people_in_db.userIds'), default=None)

    # Relationship to PeopleInDB using back_populates
    people: Optional[PeopleInDB] = relationship("PeopleInDB", back_populates="different_users")

class ClassRoster(Base):
    __tablename__ = "different_classes"

    id: int = Column(Integer, primary_key=True, index=True)
    sections_ids: Optional[List[str]] = Column(ARRAY(String), default=None)
    people_id: Optional[str] = Column(String, ForeignKey('people_in_db.SectionsIDs'), default=None)

    # Relationship to PeopleInDB using back_populates
    people: Optional[PeopleInDB] = relationship("PeopleInDB", back_populates="different_classes")

class GradebookAssociation(Base):
    __tablename__ = "different_gradebooks"

    id: int = Column(Integer, primary_key=True, index=True)
    gradebook_ids: Optional[List[str]] = Column(ARRAY(String), default=None)
    people_id: Optional[str] = Column(String, ForeignKey('people_in_db.GradebookIDs'), default=None)

    # Relationship to PeopleInDB using back_populates
    people: Optional[PeopleInDB] = relationship("PeopleInDB", back_populates="different_gradebooks")

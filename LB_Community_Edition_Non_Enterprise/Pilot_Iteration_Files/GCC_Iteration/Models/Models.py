from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional, List

Base = declarative_base()

class PeopleInDB(Base):
    __tablename__ = "people_in_db"

    AnonymizedStudentID = Column(String, primary_key=True, index=True)
    AnonymizedStudentNumber = Column(String, index=True, default=None)
    AnonymizedCounselorNumber = Column(String, index=True, default=None)
    AnonymizedHomeroomTeacherNumber = Column(String, index=True, default=None)
    GraduationCohort = Column(String, index=True, default=None)
    SchoolCode = Column(String, index=True, default=None)
    Birthdate = Column(String, default=None)
    EnabledUser = Column(String, default=None)
    Role = Column(String, default=None)
    Identifier = Column(String, default=None)
    Grades = Column(ARRAY(String), default=None)
    userIds = Column(String, index=True, default=None)
    FamilyKey = Column(ARRAY(String), default=None)
    AssociatedAccounts = Column(ARRAY(String), default=None)
    SectionsIDs = Column(ARRAY(String), default=None)
    GradebookIDs = Column(ARRAY(String), default=None)
    DateLastModified = Column(String, default=None)
    
    # Relationships using ForeignKey and back_populates
    schools = relationship("SchoolRoster", back_populates="people")
    different_users = relationship("UserAssociation", back_populates="people")
    different_classes = relationship("ClassRoster", back_populates="people")
    different_gradebooks = relationship("GradebookAssociation", back_populates="people")

class SchoolRoster(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    school_code = Column(String, index=True, default=None)
    people_id = Column(String, ForeignKey('people_in_db.SchoolCode'), default=None)

    # Relationship to PeopleInDB using back_populates
    people = relationship("PeopleInDB", back_populates="schools")

class UserAssociation(Base):
    __tablename__ = "different_users"

    id = Column(Integer, primary_key=True, index=True)
    family_key = Column(ARRAY(String), default=None)
    associated_accounts = Column(ARRAY(String), default=None)
    people_id = Column(String, ForeignKey('people_in_db.userIds'), default=None)

    # Relationship to PeopleInDB using back_populates
    people = relationship("PeopleInDB", back_populates="different_users")

class ClassRoster(Base):
    __tablename__ = "different_classes"

    id = Column(Integer, primary_key=True, index=True)
    sections_ids = Column(ARRAY(String), default=None)
    people_id = Column(String, ForeignKey('people_in_db.SectionsIDs'), default=None)

    # Relationship to PeopleInDB using back_populates
    people = relationship("PeopleInDB", back_populates="different_classes")

class GradebookAssociation(Base):
    __tablename__ = "different_gradebooks"

    id = Column(Integer, primary_key=True, index=True)
    gradebook_ids = Column(ARRAY(String), default=None)
    people_id = Column(String, ForeignKey('people_in_db.GradebookIDs'), default=None)

    # Relationship to PeopleInDB using back_populates
    people = relationship("PeopleInDB", back_populates="different_gradebooks")

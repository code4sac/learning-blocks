from sqlalchemy import Column, Integer, String, Date, Boolean, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PeopleInDB(Base):
    __tablename__ = "people_in_db"

    AnonymizedStudentID: str = Column(String, primary_key=True, index=True)
    AnonymizedStudentNumber: str = Column(String, index=True, default=None)
    AnonymizedCounselorNumber: str = Column(String, index=True, default=None)
    AnonymizedHomeroomTeacherNumber: str = Column(String, index=True, default=None)
    GraduationCohort: str = Column(String, index=True, default=None)
    SchoolCode: str = Column(String, index=True, default=None)
    Birthdate: str = Column(String, default=None)
    EnabledUser: str = Column(String, default=None)
    Role: str = Column(String, default=None)
    Identifier: str = Column(String, default=None)
    Grades: list[str] = Column(ARRAY(String), default=None)
    userIds: str = Column(String, index=True, default=None)
    FamilyKey: list[str] = Column(ARRAY(String), default=None)
    AssociatedAccounts: list[str] = Column(ARRAY(String), default=None)
    SectionsIDs: list[str] = Column(ARRAY(String), default=None)
    GradebookIDs: list[str] = Column(ARRAY(String), default=None)
    DateLastModified: str = Column(String, default=None)
    
    # Relationships using ForeignKey and back_populates
    schools: list["School"] = relationship("School", back_populates="people")
    different_users: list["DifferentUser"] = relationship("DifferentUser", back_populates="people")
    different_classes: list["DifferentClass"] = relationship("DifferentClass", back_populates="people")
    different_gradebooks: list["DifferentGradebook"] = relationship("DifferentGradebook", back_populates="people")

class School(Base):
    __tablename__ = "schools"

    id: int = Column(Integer, primary_key=True, index=True)
    school_code: str = Column(String, index=True, default=None)
    people_id: str = Column(String, ForeignKey('people_in_db.SchoolCode'), default=None)

    # Relationship to PeopleInDB using back_populates
    people: "PeopleInDB" = relationship("PeopleInDB", back_populates="schools")

class DifferentUser(Base):
    __tablename__ = "different_users"

    id: int = Column(Integer, primary_key=True, index=True)
    family_key: list[str] = Column(ARRAY(String), default=None)
    associated_accounts: list[str] = Column(ARRAY(String), default=None)
    people_id: str = Column(String, ForeignKey('people_in_db.userIds'), default=None)

    # Relationship to PeopleInDB using back_populates
    people: "PeopleInDB" = relationship("PeopleInDB", back_populates="different_users")

class DifferentClass(Base):
    __tablename__ = "different_classes"

    id: int = Column(Integer, primary_key=True, index=True)
    sections_ids: list[str] = Column(ARRAY(String), default=None)
    people_id: str = Column(String, ForeignKey('people_in_db.SectionsIDs'), default=None)

    # Relationship to PeopleInDB using back_populates
    people: "PeopleInDB" = relationship("PeopleInDB", back_populates="different_classes")

class DifferentGradebook(Base):
    __tablename__ = "different_gradebooks"

    id: int = Column(Integer, primary_key=True, index=True)
    gradebook_ids: list[str] = Column(ARRAY(String), default=None)
    people_id: str = Column(String, ForeignKey('people_in_db.GradebookIDs'), default=None)

    # Relationship to PeopleInDB using back_populates
    people: "PeopleInDB" = relationship("PeopleInDB", back_populates="different_gradebooks")

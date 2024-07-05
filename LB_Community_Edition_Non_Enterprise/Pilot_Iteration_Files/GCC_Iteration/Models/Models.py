from sqlalchemy import Column, String, ARRAY, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Optional

Base = declarative_base()

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
    Role: Mapped[Optional[str]] = mapped_column(String, default=None)
    Identifier: Mapped[Optional[str]] = mapped_column(String, ForeignKey('different_users.Identifier'), default=None)
    Grades: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), default=None)
    userIds: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    FamilyKey: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), default=None)
    SectionsIDs: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), default=None)
    GradebookIDs: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), default=None)
    DateLastModified: Mapped[Optional[str]] = mapped_column(String, default=None)
    
    # Relationships using ForeignKey and back_populates
    schools: Mapped['SchoolRoster'] = relationship("SchoolRoster", back_populates="people")
    AssociatedAccounts: Mapped[List['UserAssociation']] = relationship("UserAssociation", back_populates="people")
    different_classes: Mapped[List['ClassRoster']] = relationship("ClassRoster", back_populates="people")
    different_gradebooks: Mapped[List['GradebookAssociation']] = relationship("GradebookAssociation", back_populates="people")

class SchoolRoster(Base):
    __tablename__ = "schools"
    SchoolRosterID = Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    school_code: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    name: Mapped[Optional[str]] = mapped_column(String, index=True, default=None)

    # Relationship to PeopleInDB using back_populates
    people: Mapped[List['PeopleInDB']] = relationship("PeopleInDB", back_populates="schools")

class UserAssociation(Base):
    __tablename__ = "different_users"
    UserAssociationID = Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    Identifier: Mapped[str] = mapped_column(String, ForeignKey('people_in_db.Identifier'), primary_key=True, index=True)
    FamilyKey: Mapped[str] = mapped_column(String, ForeignKey('people_in_db.FamilyKey'), index=True) # associate with family key in people_in_db.FamilyKey
    # Relationship to PeopleInDB using back_populates
    AssociatedAccounts: Mapped['PeopleInDB'] = relationship("PeopleInDB", back_populates="AssociatedAccounts")


class ClassRoster(Base):
    __tablename__ = "different_classes"
    ClassRosterID = Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    Identifier: Mapped[str] = mapped_column(String, ForeignKey('people_in_db.Identifier'), primary_key=True, index=True)
    SectionsIDs: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), ForeignKey('people_in_db.SectionsIDs'),  index=True, default=None)

    # Relationship to PeopleInDB using back_populates
    people: Mapped['PeopleInDB'] = relationship("PeopleInDB", back_populates="different_classes")


class GradebookAssociation(Base):
    __tablename__ = "different_gradebooks"

    GradebookAssociationID = Mapped[Optional[str]] = mapped_column(String, index=True, default=None)
    Identifier: Mapped[str] = mapped_column(String, ForeignKey('people_in_db.Identifier'), primary_key=True, index=True)
    GradebookIDs: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), ForeignKey('people_in_db.GradebookIDs'),  index=True, default=None)

    # Relationship to PeopleInDB using back_populates
    people = relationship("PeopleInDB", back_populates="different_gradebooks")

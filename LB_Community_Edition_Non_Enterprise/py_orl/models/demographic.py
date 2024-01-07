from sqlalchemy import Column, String, Enum, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from models.gender import Gender
from models.status import Status
from models.true_false import TrueFalse

Base = declarative_base()


class Demographic(Base):
    """
    Demographics dataset from OneRoster.
    """
    __tablename__ = "demographic"

    sourcedId = Column(String(255), primary_key=True, unique=True, nullable=False)
    status = Column(Enum(Status), nullable=True)
    dateLastModified = Column(DateTime, nullable=True)
    birthDate = Column(DateTime, nullable=True)
    sex = Column(Enum(Gender), nullable=True)
    americanIndianOrAlaskaNative = Column(Enum(TrueFalse), nullable=True)
    asian = Column(Enum(TrueFalse), nullable=True)
    blackOrAfricanAmerican = Column(Enum(TrueFalse), nullable=True)
    nativeHawaiianOrOtherPacificIslander = Column(Enum(TrueFalse), nullable=True)
    white = Column(Enum(TrueFalse), nullable=True)
    demographicRaceTwoOrMoreRaces = Column(Enum(TrueFalse), nullable=True)
    hispanicOrLatinoEthnicity = Column(Enum(TrueFalse), nullable=True)
    countryOfBirthCode = Column(String(255), nullable=True)
    stateOfBirthAbbreviation = Column(String(255), nullable=True)
    cityOfBirth = Column(String(255), nullable=True)
    publicSchoolResidenceStatus = Column(String(255), nullable=True)
    # Metadata column
    custom_metadata = Column('metadata', JSON, nullable=True)

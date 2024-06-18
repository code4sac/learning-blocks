from pydantic import BaseModel
from typing import Optional

from models.status import Status  
from models.gender import Gender
from models.true_false import TrueFalse

class DemographicBase(BaseModel):
    sourcedId: str
    status: Optional[Status] = None
    dateLastModified: Optional[str] = None
    birthDate: Optional[str] = None
    sex: Optional[Gender] = None
    americanIndianOrAlaskaNative: Optional[TrueFalse] = None
    asian: Optional[TrueFalse] = None
    blackOrAfricanAmerican: Optional[TrueFalse] = None
    nativeHawaiianOrOtherPacificIslander: Optional[TrueFalse] = None
    white: Optional[TrueFalse] = None
    demographicRaceTwoOrMoreRaces: Optional[TrueFalse] = None
    hispanicOrLatinoEthnicity: Optional[TrueFalse] = None
    countryOfBirthCode: Optional[str] = None
    stateOfBirthAbbreviation: Optional[str] = None
    cityOfBirth: Optional[str] = None
    publicSchoolResidenceStatus: Optional[str] = None
    metadata: Optional[dict] = {}

class DemographicCreate(DemographicBase):
    pass

class DemographicUpdate(DemographicBase):
    pass

class DemographicInDBBase(DemographicBase):
    class Config:
        from_attributes  = True

class Demographic(DemographicInDBBase):
    pass

class DemographicInDB(DemographicInDBBase):
    pass

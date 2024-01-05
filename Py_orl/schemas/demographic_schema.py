from pydantic import BaseModel
from models.status import Status  # Adjust this import based on your dependencies

class DemographicBase(BaseModel):
    sourcedId: str
    status: Status
    dateLastModified: str
    birthDate: str
    sex: Status
    americanIndianOrAlaskaNative: Status
    asian: Status
    blackOrAfricanAmerican: Status
    nativeHawaiianOrOtherPacificIslander: Status
    white: Status
    demographicRaceTwoOrMoreRaces: Status
    hispanicOrLatinoEthnicity: Status
    countryOfBirthCode: str
    stateOfBirthAbbreviation: str
    cityOfBirth: str
    publicSchoolResidenceStatus: str

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

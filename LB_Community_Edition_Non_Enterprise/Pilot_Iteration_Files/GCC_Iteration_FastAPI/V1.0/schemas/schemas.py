from typing import Optional, List, Dict
from models.models import RoleEnum
from pydantic import BaseModel, Field
from datetime import datetime

# Base schema for PeopleInDB creation
class PeopleInDBCreate(BaseModel):
    firstname: str
    Lastname: str
    role: str  # Assuming it's a string, but you might want to use an Enum
    sourcedid: str
    EnabledUser: bool
    DateLastModified: Optional[str] = None
    school_code: Optional[str] = None
    AnonymizedStudentID: str 

    class Config:
        from_attributes = True

class BDDemoModel(BaseModel):
    BDcurrentAcademicIndicator: Dict[str, int] = Field(
        {
            "Suspensions_Indicator": 0,
            "EL_Prgrs_Indicator": 0,
            "Grad_Rate_Indicator": 0,
            "College_Career_Indicator": 0,
            "ELA_Indicator": 0,
            "Math_Indicator": 0,
            "Total_Students_Grad_OnTrack": 0,
            "Total_Students_Grad_OffTrack": 0,
            "Total_At_Risk_Students": 0,
        },
        description="Breakdown of students by academic indicators."
    )
    BDcurrentethnicity: Dict[str, int] = Field(
        {
            "Total_Hispanic": 0,
            "Total_White_Hispanic": 0,
            "Total_None_White_Hispanic": 0,
        },
        description="Breakdown of students by ethnicity with total counts."
    )
    BDcurrentrace: Dict[str, int] = Field(
        {
            "Total_American_Indian_Alaska_Native": 0,
            "Total_Native_Hawaiian_Other_Pacific_Islander": 0,
            "Total_White": 0,
            "Total_Black_African_American": 0,
            "Total_Asian": 0,
            "Total_Filipino": 0,
            "Total_Hispanic": 0,
            "Total_Pacific_Islander": 0,
            "Total_Two_or_more": 0,
        },
        description="Breakdown of students by race with total counts."
    )
    BDcurrentgender: Dict[str, int] = Field(
        {
            "Total_Students": 0,
            "Total_Male_Students": 0,
            "Total_Female_Students": 0,
            "Total_Non-Binary_Students": 0,
        },
        description="Breakdown of students by gender with total counts."
    )
    BDcurrentSPED: Dict[str, int] = Field(
        {
            "Total_IEP_Students": 0,
            "Total_504_Students": 0,
            "Total_Students_with_Disabilities": 0,
            "Total_Students_without_Disabilities": 0,
            "Total_Students": 0,
        }
    )
    BDcurrentLangAcq: Dict[str, int] = Field(
        {
            "Total_English_Learners": 0,
            "Total_English_Proficient": 0,
            "Total_Long_Term_English_Learners": 0,
            "Total_Reclassified_Fluent_English_Proficient": 0,
            "Total_Students": 0,
        }
    )
    BDcurrentSpclPrg: Dict[str, int] = Field(
        {
            "Total_Free_Lunch": 0,
            "Total_Reduced_Lunch": 0,
            "Total_Pay_Lunch": 0,
            "Total_Mckinney_Vento": 0,
            "Total_Foster": 0,
            "Total_Socio_Econ_Disad": 0,
            "Total_Students": 0,
            "Total_At_Risk": 0,
        }
    )
    BDcurrentAtRiskIndicators: Dict[str, int] = Field(
        {
            "Total_Free_Lunch": 0,
            "Total_Reduced_Lunch": 0,
            "Total_Pay_Lunch": 0,
            "Total_Mckinney_Vento": 0,
            "Total_Foster": 0,
            "Total_Socio_Econ_Disad": 0,
            "Total_Students": 0,
            "Total_At_Risk": 0,
        }
    )
    BDAttendance: Dict[str, int] = Field(
        {
            "Total_Days_Absent": 0,
            "Total_Days_Present": 0,
            "Total_Days_InSchl_Suspended": 0,
            "Total_Days_Home_Suspended": 0,
            "Total_Students_Suspended": 0,
            "Total_Students_Not_Suspended": 0,
            "Total_Students_Chronically_Absent": 0,
            "Total_Students_Not_Chronically_Absent": 0,
            "Total_Students_Mid_Year_Graduated": 0,
            "Total_Students_Mid_Year_Enrolled": 0,
            "Total_Students_Admin_Dropped": 0,
            "Total_Students": 0,
            "Total_Teachers": 0,
            "Change_in_Enrollment": 0,
            "perc_of_Students_Chronically_Absent": 0,
            "zero_perc_absent_current_year": 0,
            "zero_per_absent_prior_year": 0,
            "zero_to_five_perc_absent_current_year": 0,
            "zero_to_five_perc_absent_prior_year": 0,
            "five_to_ten_perc_absent_current_year": 0,
            "five_to_ten_perc_absent_prior_year": 0,
            "above_ten_perc_absent_current_year": 0,
            "above_ten_perc_absent_prior_year": 0,
        }
    )
    BDcurrentRetention: Dict[str, int] = Field(
        {
            "Total_Students_Retained": 0,
            "Total_Students": 0,
        }
    )
    BDcurrentSuspensions: Dict[str, int] = Field(
        {
            "Total_Suspensions": 0,
            "Total_InSchool_Suspensions": 0,
            "Total_OutOfSchool_Suspensions": 0,
            "Total_Students": 0,
        }
    )
    BDCurrentweeklyEnrollmentCurrentYear: Dict[str,int] = Field(
        {
            "2024_2025_week_01": 0,
            "2024_2025_week_02": 0,
            "2024_2025_week_03": 0,
            "2024_2025_week_04": 0,
            "2024_2025_week_05": 0,
            "2024_2025_week_06": 0,
            "2024_2025_week_07": 0,
            "2024_2025_week_08": 0,
            "2024_2025_week_09": 0,
            "2024_2025_week_10": 0,
            "2024_2025_week_11": 0,
            "2024_2025_week_12": 0,
            "2024_2025_week_13": 0,
            "2024_2025_week_14": 0,
            "2024_2025_week_15": 0,
            "2024_2025_week_16": 0,
            "2024_2025_week_17": 0,
            "2024_2025_week_18": 0,
            "2024_2025_week_19": 0,
            "2024_2025_week_20": 0,
            "2024_2025_week_21": 0,
            "2024_2025_week_22": 0,
            "2024_2025_week_23": 0,
            "2024_2025_week_24": 0,
            "2024_2025_week_25": 0,
            "2024_2025_week_26": 0,
            "2024_2025_week_27": 0,
            "2024_2025_week_28": 0,
            "2024_2025_week_29": 0,
            "2024_2025_week_30": 0,
            "2024_2025_week_31": 0,
            "2024_2025_week_32": 0,
            "2024_2025_week_33": 0,
            "2024_2025_week_34": 0,
            "2024_2025_week_35": 0,
            "2024_2025_week_36": 0,
            "2024_2025_week_37": 0,
            "2024_2025_week_38": 0,
            "2024_2025_week_39": 0,
            "2024_2025_week_40": 0,
        }
    )
    BDPriorYearWeeklyEnrollment: Dict[str,int] = Field(
        {
            "2023_2024_week_01": 0,
            "2023_2024_week_02": 0,
            "2023_2024_week_03": 0,
            "2023_2024_week_04": 0,
            "2023_2024_week_05": 0,
            "2023_2024_week_06": 0,
            "2023_2024_week_07": 0,
            "2023_2024_week_08": 0,
            "2023_2024_week_09": 0,
            "2023_2024_week_10": 0,
            "2023_2024_week_11": 0,
            "2023_2024_week_12": 0,
            "2023_2024_week_13": 0,
            "2023_2024_week_14": 0,
            "2023_2024_week_15": 0,
            "2023_2024_week_16": 0,
            "2023_2024_week_17": 0,
            "2023_2024_week_18": 0,
            "2023_2024_week_19": 0,
            "2023_2024_week_20": 0,
            "2023_2024_week_21": 0,
            "2023_2024_week_22": 0,
            "2023_2024_week_23": 0,
            "2023_2024_week_24": 0,
            "2023_2024_week_25": 0,
            "2023_2024_week_26": 0,
            "2023_2024_week_27": 0,
            "2023_2024_week_28": 0,
            "2023_2024_week_29": 0,
            "2023_2024_week_30": 0,
            "2023_2024_week_31": 0,
            "2023_2024_week_32": 0,
            "2023_2024_week_33": 0,
            "2023_2024_week_34": 0,
            "2023_2024_week_35": 0,
            "2023_2024_week_36": 0,
            "2023_2024_week_37": 0,
            "2023_2024_week_38": 0,
            "2023_2024_week_39": 0,
            "2023_2024_week_40": 0,
        }
    )
    BDPriorPriorYearWeeklyEnrollment: Dict[str,int] = Field(
        {
            "2022_2023_week_01": 0,
            "2022_2023_week_02": 0,
            "2022_2023_week_03": 0,
            "2022_2023_week_04": 0,
            "2022_2023_week_05": 0,
            "2022_2023_week_06": 0,
            "2022_2023_week_07": 0,
            "2022_2023_week_08": 0,
            "2022_2023_week_09": 0,
            "2022_2023_week_10": 0,
            "2022_2023_week_11": 0,
            "2022_2023_week_12": 0,
            "2022_2023_week_13": 0,
            "2022_2023_week_14": 0,
            "2022_2023_week_15": 0,
            "2022_2023_week_16": 0,
            "2022_2023_week_17": 0,
            "2022_2023_week_18": 0,
            "2022_2023_week_19": 0,
            "2022_2023_week_20": 0,
            "2022_2023_week_21": 0,
            "2022_2023_week_22": 0,
            "2022_2023_week_23": 0,
            "2022_2023_week_24": 0,
            "2022_2023_week_25": 0,
            "2022_2023_week_26": 0,
            "2022_2023_week_27": 0,
            "2022_2023_week_28": 0,
            "2022_2023_week_29": 0,
            "2022_2023_week_30": 0,
            "2022_2023_week_31": 0,
            "2022_2023_week_32": 0,
            "2022_2023_week_33": 0,
            "2022_2023_week_34": 0,
            "2022_2023_week_35": 0,
            "2022_2023_week_36": 0,
            "2022_2023_week_37": 0,
            "2022_2023_week_38": 0,
            "2022_2023_week_39": 0,
            "2022_2023_week_40": 0,
        }
    )     
    BDweeklyEnrollmentByGrade: Dict[str,int] = Field(
        {
            "TK": 0,
            "K": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
        }
    )




class TeacherInDBCreate(BaseModel):
    AnonymizedTeacherID: str
    AnonymizedTeacherNumber: Optional[str] = None
    Sections: Optional[List[str]] = None
    StuAssociated: Optional[List[str]] = None
    SchlAssociated: Optional[str] = None
    Credentials: Optional[List[str]] = None
    Subjects: Optional[List[str]] = None
    SiteDuties: Optional[List[str]] = None
    GradeLevels: Optional[List[str]] = None
    bddemo: Optional[BDDemoModel] = None

    class Config:
        from_attributes = True

# Response schema for PeopleInDB

class StudentInDBCreate(BaseModel):
    AnonymizedStudentID: str
    AnonymizedStudentNumber: str
    Sections: Optional[List[str]] = None
    SchlAssociated: Optional[str] = None
    Birthdate: Optional[str] = None
    role: RoleEnum = "student"
    sourcedid: str
    school_code: Optional[str] = None
    bddemo: Optional[BDDemoModel] = None
    school_name: Optional[str] = None



 #Response schema for StudentInDB
class StudentInDBResponse(BaseModel):
    AnonymizedStudentID: str
    AnonymizedStudentNumber: Optional[str] = None
    role: RoleEnum = "student"
    sourcedid: str
    id: int
    birthdate: Optional[str] = None
    Sections: Optional[List[str]] = None
    SchlAssociated: Optional[str] = None
    school_code: Optional[str] = None
    bddemo: Optional[BDDemoModel] = None
    

    class Config:
      from_attributes = True
      




# Response schema for TeacherInDB
class TeacherInDBResponse(BaseModel):
    AnonymizedTeacherID: str
    AnonymizedTeacherNumber: Optional[str] = None
    role: RoleEnum = "teacher"
    sourcedid: str
    StuAssociated: List[StudentInDBResponse] = []
    SchlAssociated: Optional[str] = None
    Credentials: Optional[List[str]] = None
    Subjects: Optional[List[str]] = None
    SiteDuties: Optional[List[str]] = None
    GradeLevels: Optional[List[str]] = None
    EnabledUser: Optional[str] = None
    school_code: Optional[str] = None
    bddemo: Optional[BDDemoModel] = None
    DateLastModified: Optional[str] = None
    Sections: Optional[List[str]] = None



    class Config:
      from_attributes = True


class PeopleInDB(BaseModel):
    id: int
    firstname: str
    Lastname: str
    role: RoleEnum
    sourcedid: str
    EnabledUser: Optional[str] = None
    dateLastModified: Optional[str] = None
    school_code: Optional[str] = None
    student: Optional[StudentInDBResponse] = None
    teacher: Optional[TeacherInDBResponse] = None
    class Config:
        orm_mode = True

class PeopleInDBResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    role: str
    sourcedid: str
    EnabledUser: bool
    dateLastModified: Optional[str] = None
    school_code: Optional[str]
    student: Optional[StudentInDBResponse] = None
    teacher: Optional[TeacherInDBResponse] = None

    class Config:
        orm_mode = True
# Base schema for SchoolsInDB

class SchoolsInDBBase(BaseModel):
    school_code: str
    school_name: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None

    class Config:
        orm_mode = True

# Schema for SchoolsInDB creation
class SchoolsInDBCreate(SchoolsInDBBase):
    bddemo : Optional[BDDemoModel] = None
    pass

# Response schema for SchoolsInDB with list of associated people
class SchoolsInDBResponse(SchoolsInDBBase):
    id: int
    people: List[PeopleInDBResponse] = []  # List of people associated with the school
    school_code: str
    school_name: str

    bddemo: Optional[BDDemoModel] = None

    class Config:
        orm_mode = True

# Schema for updating PeopleInDB records
class PeopleInDBUpdate(BaseModel):
    firstname: Optional[str] = None
    Lastname: Optional[str] = None
    role: RoleEnum = "RoleEnum"
    sourcedid: Optional[str] = None
    EnabledUser: Optional[str] = None
    dateLastModified: Optional[str] = None
    school_code: Optional[str] = None

    class Config:
        from_attributes = True

class StudentInDB(BaseModel):
    id: int
    AnonymizedStudentID: str
    AnonymizedStudentNumber: str
    Sections: Optional[List[str]] = None
    SchlAssociated: Optional[str] = None
    Birthdate: Optional[str] = None
    school_code: Optional[str] = None

    class Config:
        orm_mode = True


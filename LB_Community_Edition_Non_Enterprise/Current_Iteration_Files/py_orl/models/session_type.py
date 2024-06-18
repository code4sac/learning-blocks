from enum import Enum


class SessionType(str, Enum):
    GradingPeriod = 'gradingPeriod'
    Semester = 'semester'
    SchoolYear = 'schoolYear'
    Term = 'term'

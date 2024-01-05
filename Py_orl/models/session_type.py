from enum import Enum


class SessionType(Enum):
    GradingPeriod = 'gradingPeriod'
    Semester = 'semester'
    SchoolYear = 'schoolYear'
    Term = 'term'

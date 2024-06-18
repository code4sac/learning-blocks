from enum import Enum


class ScoreStatus(str, Enum):
    Exempt = 'exempt'
    FullyGraded = 'fully graded'
    NotSubmitted = 'not submitted'
    PartiallyGraded = 'partially graded'
    Submitted = 'submitted'

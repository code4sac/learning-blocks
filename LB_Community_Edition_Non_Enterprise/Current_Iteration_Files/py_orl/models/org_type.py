from enum import Enum


class OrgType(str, Enum):
    Department = 'department'
    School = 'school'
    District = 'district'
    Local = 'local'
    State = 'state'
    National = 'national'

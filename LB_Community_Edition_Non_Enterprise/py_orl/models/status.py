from enum import Enum


class Status(Enum):
    Active = 'active'
    ToBeDeleted = 'tobedeleted'
    Inactive = 'inactive'

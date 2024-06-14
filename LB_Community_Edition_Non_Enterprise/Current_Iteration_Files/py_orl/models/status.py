from enum import Enum


class Status(str, Enum):
    Active = 'active'
    ToBeDeleted = 'tobedeleted'
    Inactive = 'inactive'

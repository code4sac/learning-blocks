from enum import Enum


class Gender(str, Enum):
    Male = 'male'
    Female = 'female'
    NoneBinary = 'nonbinary'


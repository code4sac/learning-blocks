from enum import Enum


class RoleType(Enum):
    Administrator = 'administrator'
    Aide = 'aide'
    Guardian = 'guardian'
    Parent = 'parent'
    Proctor = 'proctor'
    Relative = 'relative'
    Student = 'student'
    Teacher = 'teacher'

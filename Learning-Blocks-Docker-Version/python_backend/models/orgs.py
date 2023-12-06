from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean, Enum

from db.base_class import Base


class Orgs(Base):
    """
    I added boolean columns for each level of the hierarchy (national, state, local, district, school).
    These columns are used to mark whether an organization is of that level.
    For example, if an organization is a state, the state column will be set to True, and so on.
    I added is_department method to check if the organization is a department based on the "type" column.
    I added methods (e.g., is_national, is_state, etc.)
    to check the level of the organization based on the boolean columns.
    This allows you to maintain the explicit hierarchy and department information in the database alongside the "type"
    of the organization.
    You can use the boolean columns and methods to easily determine the level and type of an organization.
    I need to check if there are more hierarchies
    """
    id = Column(Integer, primary_key=True, index=True)
    sourcedId = Column(String(36), index=True, unique=True)
    status = Column(Enum('active', 'tobedeleted', 'inactive', name='enum1'))
    dateLastModified = Column(DateTime(timezone=True))
    name = Column(String(36))
    type = Column(Enum('department', 'school', 'district', 'local', 'state', 'national', name='enum_type'))
    identifier = Column(String)
    parentSourcedId = Column(String(36), ForeignKey("orgs.sourcedId"))

    # Hierarchy
    national = Column(Boolean, default=False)
    state = Column(Boolean, default=False)
    local = Column(Boolean, default=False)
    district = Column(Boolean, default=False)
    school = Column(Boolean, default=False)

    def is_department(self):
        """
        check if the organization is a department based on the "type" column.
        """
        return self.type == 'department'

    def is_national(self):
        """
        check the level of the organization based on the boolean columns.
        """
        return self.national

    def is_state(self):
        """
        check the level of the organization based on the boolean columns.
        """
        return self.state

    def is_local(self):
        """
        check the level of the organization based on the boolean columns.
        """
        return self.local

    def is_district(self):
        """
        check the level of the organization based on the boolean columns.
        """
        return self.district

    def is_school(self):
        """
        check the level of the organization based on the boolean columns.
        """
        return self.school

from sqlalchemy import Column, String, Enum, Integer, DateTime, ForeignKey

from db.base_class import Base

'''
I added boolean columns for each level of the hierarchy (national, state, local, district, school). These columns are used to mark whether an organization is of that level. For example, if an organization is a state, the state column will be set to True, and so on.

I added a is_department method to check if the organization is a department based on the "type" column.

I added methods (e.g., is_national, is_state, etc.) to check the level of the organization based on the boolean columns.

This allows you to maintain the explicit hierarchy and department information in the database alongside the "type" of the organization. You can use the boolean columns and methods to easily determine the level and type of an organization.

I need to check if their are more hierarchies
'''
class Orgs(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    sourcedId = Column(String(36), unique=True, nullable=False)
    status = Column(Enum('active', 'tobedeleted', 'inactive', name='enum1'), nullable=False)
    dateLastModified = Column(DateTime, nullable=False)
    name = Column(String, nullable=False)
    type = Column(Enum('department', 'school', 'district', 'local', 'state', 'national', name='enum_type'),
                  nullable=False)
    identifier = Column(String)
    parentSourcedId = Column(String(36), ForeignKey("orgs.sourcedId"))

    # Hierarchy
    national = Column(Boolean, default=False)
    state = Column(Boolean, default=False)
    local = Column(Boolean, default=False)
    district = Column(Boolean, default=False)
    school = Column(Boolean, default=False)

    def is_department(self):
        return self.type == 'department'

    def is_national(self):
        return self.national

    def is_state(self):
        return self.state

    def is_local(self):
        return self.local

    def is_district(self):
        return self.district

    def is_school(self):
        return self.school
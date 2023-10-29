from sqlalchemy import Column, String, Enum, DateTime, Date
from db.base_class import Base

class academicsessions(Base):


    sourcedId = Column(String(256), primary_key=True, unique=True, nullable=False)
    status = Column(Enum('active', 'tobedeleted', 'inactive', name='enum1'), nullable=False)
    dateLastModified = Column(DateTime)
    title = Column(String)
    type = Column(Enum('gradingPeriod', 'semester', 'schoolYear', 'term', name='enum2'), nullable=False)
    startDate = Column(Date)
    endDate = Column(Date)
    parentSourcedId = Column(String(256), primary_key=True, unique=True, nullable=False)
from sqlalchemy import Table, Column, ForeignKey, String
from db.base_class import Base

class_term = Table(
    "class_term",
    Base.metadata,
    Column("classSourcedId", String(255), ForeignKey("class.sourcedId"), primary_key=True),
    Column("termSourcedId", String(255), ForeignKey("academic_session.sourcedId"), primary_key=True),
)

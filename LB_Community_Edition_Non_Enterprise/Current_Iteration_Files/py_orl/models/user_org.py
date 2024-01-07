from sqlalchemy import Table, Column, ForeignKey, String
from db.base_class import Base

user_org = Table(
    "user_org",
    Base.metadata,
    Column("userSourcedId", String(255), ForeignKey("user.sourcedId"), primary_key=True),
    Column("orgSourcedId", String(255), ForeignKey("org.sourcedId"), primary_key=True),
)

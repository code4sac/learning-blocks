from sqlalchemy import Table, Column, ForeignKey, String
from db.base_class import Base

user_agent = Table(
    "user_agent",
    Base.metadata,
    Column("userSourcedId", String(255), ForeignKey("user.sourcedId"), primary_key=True),
    Column("agentSourcedId", String(255), ForeignKey("user.sourcedId"), primary_key=True),
)

from sqlalchemy import Column, Integer, String

from db.base_class import Base


class Org(Base):
    source_id: int = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

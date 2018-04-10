from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .meta import Base

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)

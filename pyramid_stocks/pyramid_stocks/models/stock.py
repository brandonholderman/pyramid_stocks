from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from .meta import Base

class Stock(Base):
    __tablename__= 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    companyName = Column(String, nullable=False, unique=True)
    website = Column(String)
    industry = Column(String)
    sector = Column(String)
    CEO = Column(String)
    issueType = Column(String)
    exchange = Column(String)
    description = Column(String)

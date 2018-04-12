from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from .meta import Base

class Stock(Base):
    __tablename__= 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    companyName = Column(String, nullable=False, unique=True)
    industry = Column(String)
    website = Column(String)
    sector = Column(String)
    CEO = Column(String)
    issueType = Column(String)
    exchange = Column(String)
    description = Column(String)


Index('entry_index', Stock.id, unique=True, mysql_length=255)

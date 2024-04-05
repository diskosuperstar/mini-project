from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

# SQLAlchemy model for metadata
class Metadata(Base):
    __tablename__ = 'table_column_metadata'
    __table_args__ = {'schema': 'catalog'}

    id = Column(Integer, primary_key=True)
    table_name = Column(String)
    column_name = Column(String)
    data_type = Column(String)
    is_active = Column(Boolean, default=True, nullable=False)

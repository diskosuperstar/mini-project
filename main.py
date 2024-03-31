from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection URL
database_url = os.getenv('METADATA_DATABASE_URL')

# Create engine
engine = create_engine(database_url)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Base class for SQLAlchemy models
Base = declarative_base()

# SQLAlchemy model for metadata
class Metadata(Base):
    __tablename__ = 'metadata'
    __table_args__ = {'schema': 'catalog'}

    id = Column(Integer, primary_key=True)
    table_name = Column(String)
    column_name = Column(String)
    data_type = Column(String)

# Pydantic model for metadata
class MetadataBase(BaseModel):
    table_name: str
    column_name: str
    data_type: str

class MetadataCreate(MetadataBase):
    pass

class MetadataRead(MetadataBase):
    id: int

# Create tables
Base.metadata.create_all(engine)
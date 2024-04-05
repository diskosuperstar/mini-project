from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from models import Base, Metadata
from schemas import MetadataCreate
from typing import List

# Load environment variables
load_dotenv(".env")

# Database connection URL
source_database_url = os.getenv('SOURCE_DATABASE_URL')

# Create engine
engine = create_engine(source_database_url)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

def get_metadata(table_name: str, schema_name: str):
    metadata = Metadata()
    columns_table = Table(table_name, metadata, autoload_with=engine, schema=schema_name)

    return columns_table


metadata = MetaData()
columns_table = Table('columns', metadata, autoload_with=engine, schema='information_schema')




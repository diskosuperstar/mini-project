from dotenv import load_dotenv
from urllib.parse import quote
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_database_url():
    # Load the .env file
    load_dotenv()

    # Get the database connection components from the .env file
    username = os.getenv('DB_USERNAME')
    password = quote(os.getenv('DB_PASSWORD'))  # URL encode the password
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    driver = os.getenv('DB_DRIVER')

    # Construct and return the connection string
    return f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"

# Create engine
engine = create_engine(get_database_url())

# Create session
Session = sessionmaker(bind=engine)
session = Session()
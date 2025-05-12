from sqlalchemy import create_engine
import os

port = 5432

def get_engine():
    #insert user credentials
    username = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASS", "your_password")
    host = os.getenv("DB_HOST", "localhost")
    database = os.getenv("DB_NAME", "spotify_db")

    return create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

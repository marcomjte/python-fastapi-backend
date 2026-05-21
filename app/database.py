# app/database.py
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

user     = os.getenv("DB_USER", "root")
password = quote_plus(os.getenv("DB_PASSWORD", ""))
host     = os.getenv("DB_HOST", "localhost")
port     = os.getenv("DB_PORT", "3306")
name     = os.getenv("DB_NAME", "myapp")

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from dotenv import load_dotenv
import os
from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

load_dotenv()

""" We can add a database url environment file and load"""
# DATABASE_URL = os.getenv('DATABASE_URL')

""" USE SQLITE"""
# DATABASE_URL = 'sqlite:///./todosapp.db'

""" HARD CODED POSTGRESQL"""
DATABASE_URL = "postgresql://postgres:postgres@db:5432/cleanfastapi"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
        
    finally:
        db.close()
        
DbSession = Annotated[Session, Depends(get_db)]


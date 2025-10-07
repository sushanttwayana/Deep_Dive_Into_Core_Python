from fastapi import FastAPI
from src.database.core import engine, Base
from src.entities import todo # Import models to register them
from src.entities import user
from src.api import register_routes
from src.logging import configure_logging, LogLevels

configure_logging(LogLevels.info)

app = FastAPI()

"""
    Only uncomment below to create a new table, otherwise the tests will fail if not connceted
"""

# Base.metadata.create_all(bind=engine)

register_routes(app)
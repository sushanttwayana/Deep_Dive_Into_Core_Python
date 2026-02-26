from sqlalchemy import create_engine    
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# postgres connection
# postgres_url = "postgresql://<username>:<password>@<host>:<port>/<database_name>"

# postgres_url = "postgresql+psycopg2://postgres:Sushant@45#@localhost:5432/postgres"

# #mysql connection
# mysql_url = "mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>"

# #oracle connection
# oracle_url = "oracle+cx_oracle://<username>:<password>@<host>:<port>/<database_name>"


db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)


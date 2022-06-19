from sqlalchemy import (
    MetaData,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .uri_post import PostgresURI


# -- Single Responsibility
# Separated the class get_postgres_uri from models


#Creating base, engine and session objects
Base = declarative_base(
    metadata=MetaData(),
)


engine = create_engine(
    PostgresURI.get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)

local_session = sessionmaker(autoflush=False,
                             autocommit=False, bind=engine)

# create db session
db = local_session()

# each class model is in its one file, SRP

def start_mappers():
    Base.metadata.create_all(engine)

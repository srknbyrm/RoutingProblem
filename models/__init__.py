from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

engine = create_engine("postgresql://postgres:123456@localhost:5432/RoutingProjectDB")
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)

Base = declarative_base()

from .Locations import Location
from .Route import Route
from .Location_Route import LocationRoute

Base.metadata.create_all(engine)

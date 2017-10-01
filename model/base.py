from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("mysql://root:Hero2of1war@localhost/library_system")
Base = declarative_base()
Base.metadata.create_all(engine)
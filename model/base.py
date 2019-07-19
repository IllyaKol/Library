from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("mysql://root:******@localhost/library_system")
Base = declarative_base()
Base.metadata.create_all(engine)

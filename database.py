from lib2to3.pytree import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database NAme : address.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./address.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
)

# Creates instance of sessionlocal for each database session.
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

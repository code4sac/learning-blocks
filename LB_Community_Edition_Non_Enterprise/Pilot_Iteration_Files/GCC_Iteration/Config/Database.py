from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

# SQLAlchemy engine setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal class to create sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

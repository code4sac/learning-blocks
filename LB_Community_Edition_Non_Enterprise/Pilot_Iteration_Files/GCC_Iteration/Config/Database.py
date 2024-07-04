"""
Step 1: Create database.py
First, define database.py to set up the SQLAlchemy engine and sessionmaker:
# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection URL
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/dbname"

# SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal class for creating session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""

"""
Step 2: Use SessionLocal in main.py
Next, use SessionLocal in your main.py or wherever you need to interact with the database:
# main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from app import models  # Import all models to ensure they are registered with SQLAlchemy

# Create FastAPI app instance
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example route handler using database session
@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()

if __name__ == "__main__":
    # Create database tables (if not exists) using SQLAlchemy
    models.Base.metadata.create_all(bind=engine)

    # Run the FastAPI application
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


"""
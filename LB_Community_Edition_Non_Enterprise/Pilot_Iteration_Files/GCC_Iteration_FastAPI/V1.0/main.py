from fastapi import FastAPI
from routers import people, students
from databases.databases import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

# Define FastAPI app
app = FastAPI()

# Include routers
app.include_router(people.router)
app.include_router(students.router)

#!/bin/bash

# Define the path to the migrations directory
MIGRATIONS_DIR="/app/alembic/versions"

# Function to delete all migration versions
delete_all_migrations() {
  echo "Deleting all migration versions..."
  
  # Remove all migration files in the versions directory
  rm -f $MIGRATIONS_DIR/*.py
  
  # Remove the __init__.py file if it exists
  rm -f $MIGRATIONS_DIR/__init__.py
  
  echo "All migration versions deleted."
}

# Delete all existing migrations
delete_all_migrations

# Try to apply the latest migration
echo "Attempting to apply the latest migration..."
docker-compose run --rm app alembic upgrade head

# Check if the previous command failed
if [ $? -ne 0 ]; then
  echo "Migration failed. Generating a new migration script..."
  
  # Generate a new migration script with a message
  docker-compose run --rm app alembic revision --autogenerate -m "update model_peopleindb_grades_totaketuplelist"

  # Apply the latest migration again
  echo "Applying the new migration..."
  docker-compose run --rm app alembic upgrade head
fi

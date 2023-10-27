# Learning Blocks Backend

This is an overview of how to run Learning Blocks without Docker. It describes setting up the project and running the
local server.

## Development URLs

Development URLs, for local development.

Backend: http://localhost/api/v1/

Automatic Interactive Docs (Swagger UI): https://localhost/docs

pgAdmin: http://localhost:5050

## Project setup

The project requires Python and PostgresSQL to be installed.

### Python

**See:
** [Stand_alone_FastAPI_setup.md#python-virtual-environment](/Documentation%20Directory/Stand_alone_FastAPI_setup.md)

1. Set up a Python virtual environment
2. Install the project dependencies listed
   in [requirements.txt](/Learning-Blocks-No-Docker-Version/py_orl/requirements.txt).

> Make sure the `venv` folder is in the root of the [py_orl](/Learning-Blocks-No-Docker-Version/py_orl) folder.
> This ensures that app Python files (crude, api, etc.) are imported correctly.

### PostgreSQL database

**See:** [Database_documentation.md](/Documentation%20Directory/Database_documentation.md)

1. Install PostgreSQL
2. Create an admin user and table for the application.
3. Add environment variables for database credentials and
   other [configuration settings](/Learning-Blocks-No-Docker-Version/py_orl/core/config.py).
4. (Optional) Install pgAdmin to view and modify the database.

## Local server

**See:**  [Stand_alone_FastAPI_setup.md#fastapi-examples](/Documentation%20Directory/Stand_alone_FastAPI_setup.md)

You can initialize the database with the following commands:

```shell
alembic upgrade head
python initial_data.py
```

Run the FastAPI server.

```shell
export project_name="Learning Blocks"
python -m uvicorn app:app --reload
``` 

## Run with Make

> More commands can be found in [Makefile](/Learning-Blocks-No-Docker-Version/py_orl/Makefile).

### make local

Run the local server.

### make test

Run all tests.

### make coverage

Run test coverage.

### make migrate

Execute the latest database migrations.

### make init

Initialize database with example data.

### make lint

Check and optimize code formatting. 



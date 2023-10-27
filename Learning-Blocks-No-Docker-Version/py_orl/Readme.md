# Learning Blocks Backend

This is an overview of how to run Learning Blocks without Docker. It describes setting up the project and running the
local server.

## Project setup

The project requires Python and PostgreSQL to be installed.

### Python

**See:** [Stand_alone_FastAPI_setup.md#python-virtual-environment](Stand_alone_FastAPI_setup.md)

1. Set up a Python virtual environment
2. Install the project dependencies listed in [requirements.txt](requirements.txt).

> Make sure the `venv` folder is in the root of the [py_orl](.) folder. This ensures that app Python files (crude, api,
> etc.) are imported correctly.

### PostgreSQL database

**See:** [Database_documentation.md](/Documentation%20Directory/Database_documentation.md)

1. Install PostgreSQL
2. Create an admin user and table for the application.
3. (Optional) Install pgAdmin to view and modify the database.

## Local server

**See:**  [Stand_alone_FastAPI_setup.md#fastapi-examples](#fastapi-examples-Stand_alone_FastAPI_setup.md)

Run the FastAPI server.

```shell
uvicorn app:app --reload
``` 

## Running with Make

> More commands can be found in
> [scripts/Readme.md](scripts/Readme.md), [scripts/Makefile](scripts/Makefile), and [tests/Makefile](tests/Makefile).

### make local

Run the local server.

### make migrate

Execute the latest database migrations.

### make init

Initialize database with example data.

### make test

Run all tests.

### make coverage

Run test coverage.




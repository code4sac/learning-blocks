# Learning Blocks Enterprise FastAPI

This is an overview of how to run Learning Blocks without Docker. It describes setting up the project and running the
local server.
> For more information, view the [Documentation Directory](/Documentation%20Directory)

## Getting started.

Install PostgreSQL and the Python dependencies. For help,
see [No_docker_getting_started.md](Documentation%20Directory/No_docker_getting_started.md).

### Add environment variables

Add the following environment variables to your path. You can also try to create a .env file, but I haven't tested that
this works.

#### .env

```dotenv
# The application is configured to use only lowercase environment variable names. Example: lower_case=AnythiNGelseUPPER023~#=. The names are case-sensative.
DOMAIN=localhost

# Backend
PROJECT_NAME="Learning Blocks"

# Postgres
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=change_me_password01
POSTGRES_DB=app

# PgAdmin
PGADMIN_LISTEN_PORT=5050
PGADMIN_DEFAULT_EMAIL=user
PGADMIN_DEFAULT_PASSWORD=change_me_password01
```

### Initialize the database

Create a database with the same name as the POSTGRES_DB environment variable. Then, run the Alembic migration to
initialize the database tables. To populate the database with data, run the initial_data.py script.

```shell
alembic upgrade head
python initial_data.py
```

### Run the server

With `uvicorn app:app --reload` running, you should be able to navigate to localhost:8000 in your browser. Verify it is
running by viewing [localhost:8000/docs](http://localhost:8000/docs).

```shell
# Before running, install python packages in a virtual environment.
python -m uvicorn app:app --reload
```

You can also start the server with `make local`. View other commands in
the [Makefile](/Learning-Blocks-No-Docker-Version/py_orl/Makefile).

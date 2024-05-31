# Learning Blocks with Docker

This project is under development. It currently runs the FastAPI server but not the database.

## Getting Started

Create a .env file with your database credentials. The docker-compose.yml uses these environment variables in the `environment:` section.

#### .env
```dotenv
# The application is configured to use only lowercase environment variable names. Example: lower_case=AnythiNGelseUPPER023~#=. The names are case-sensative.
domain=localhost

# Backend
project_name="Learning Blocks"

# Postgres
postgres_server=localhost
postgres_user=postgres
postgres_password=change_me_password01
postgres_db=app

# PgAdmin
pgadmin_listen_port=5050
pgadmin_default_email=user
pgadmin_default_password=change_me_password01
```

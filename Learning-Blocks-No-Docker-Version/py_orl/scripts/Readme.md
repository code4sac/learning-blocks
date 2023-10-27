# Backend API Scripts for Learning Blocks

These files help run different steps of the project. They can be copied and pasted in your terminal or run with Make.

## Copy & Paste

You can initialize the database with the following command:

```shell
python backend_pre_start.py
alembic upgrade head
python initial_data.py
```

Then, run the local webserver.

```shell
export project_name="Learning Blocks"
python -m uvicorn app:app --reload
```

## Running with Make

### make dev

Run the local server

### make migrate

Execute the latest database migrations.

### make init

Initialize database with example data.

### make lint

Check and optimize code formatting. 


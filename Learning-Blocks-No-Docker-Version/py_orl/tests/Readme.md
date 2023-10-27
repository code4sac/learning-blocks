# Tests for Learning Blocks

The tests folder contains everything related to testing Learning Blocks.

## Copy & Paste


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

### make local

Run the local server

### make migrate

Execute the latest database migrations.

### make init

Initialize database with example data.

### make test

### make coverage


# Run the local server.
local:
	make -C scripts dev

# Execute the latest database migrations.
migrate:
	make -C scripts migrate

# Initialize database with example data.
init:
	make -C scripts init

# Run all tests.
test:
	make -C tests all

# Run test coverage.
coverage:
	make -C tests coverage


# Run the web server locally.
dev:
	python -m uvicorn app:app --reload

# Let the DB start and run migrations.
migrate:
	python backend_pre_start.py
	alembic upgrade head

# Create initial data in DB. Requires a migration first.
init:migrate
	python initial_data.py

# Check and optimize code formatting.
lint:
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app --exclude=__init__.py
	mypy app
	black app --check
	isort --force-single-line-imports app
	flake8
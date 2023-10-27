# Run the web server locally.
local:
	python -m uvicorn app:app --reload

# Run all tests.
test:
	python -m pytest --cov-report=term-missing tests

# Run test coverage.
coverage:
	python -m pytest --cov-report=html

# Run Alembic database migration upgrade.
migrate:
	alembic upgrade head

# Initialize database with example data. Requires a migration first.
init:migrate
	python initial_data.py

# Check and optimize code formatting.
lint:
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app --exclude=__init__.py
	mypy app
	black app --check
	isort --force-single-line-imports app
	flake8
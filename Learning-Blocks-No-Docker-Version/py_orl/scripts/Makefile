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
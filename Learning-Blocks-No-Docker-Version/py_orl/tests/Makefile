# Run all tests.
all:
	python tests_pre_start.py
	pytest --cov=app --cov-report=term-missing tests "${@}"

# Run test coverage.
coverage:
	bash scripts/test.sh --cov-report=html "${@}"
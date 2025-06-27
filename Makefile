.PHONY: install test lint format coverage run

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run pre-commit run --all-files

format:
	poetry run black .

coverage:
	poetry run pytest --cov=powertrak --cov-report=html

run:
	poetry run powertrak

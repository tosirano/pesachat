.PHONY: install migrate dev test lint format

install:
	poetry install

migrate:
	poetry run alembic upgrade head

dev:
	poetry run pesachat-bot & poetry run pesachat-core

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run black .

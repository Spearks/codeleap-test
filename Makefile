bare-install:
	pip3 install poetry
	poetry install --no-dev
bare-migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
bare-test:
	poetry run python3 manage.py test
bare-run:
	poetry run gunicorn careers.wsgi -b 0.0.0.0
# Docker commands
build:
	docker compose build
migrate:
	LOGGING=none MIGRATE=true docker compose up --force-recreate
test:
	LOGGING=none MIGRATE=false TEST=true docker compose up --force-recreate
run:
	docker compose up --force-recreate
install:
	poetry install

update:
	poetry update

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

shell:
	$ ./manage.py shell

test:
	poetry run python3 manage.py test

lint:
	poetry run flake8 task_manager

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

selfcheck:
	poetry check

check:	selfcheck test-coverage lint

trans-messages:
	python manage.py makemessages -l ru

compile-trans:
	python manage.py compilemessages

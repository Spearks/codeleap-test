#!/bin/sh

if [ "$MIGRATE" ==   "True" ]
then
    python3 manage.py makemigrations
    python3 manage.py migrate
fi

python3 manage.py test

/app/.venv/bin/gunicorn careers.wsgi -b 0.0.0.0

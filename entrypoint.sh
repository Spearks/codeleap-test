#!/bin/sh
# Just migrate the application

if [ "$MIGRATE" = "true" ]
then
    python3 manage.py makemigrations --noinput
    python3 manage.py migrate --noinput
    exit 0  
fi

# Just test the application
if [ "$TEST" = "true" ]
then
    python3 manage.py test
    exit 0
fi

python3 manage.py collectstatic --noinput

python3 manage.py test

python3 manage.py runserver 0.0.0.0:8000
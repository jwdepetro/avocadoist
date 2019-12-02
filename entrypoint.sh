#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput

if [ "$DEBUG" = 1 ]; then
    echo "starting gunicorn for development"
    gunicorn --bind 0.0.0.0:8002 --reload app.wsgi:application
else
    echo "starting gunicorn"
    gunicorn --bind 0.0.0.0:8002 app.wsgi:application
fi
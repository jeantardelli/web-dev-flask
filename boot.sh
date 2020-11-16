#!/bin/sh

echo "Waiting for MySQL..."

while ! nc -z database 3306; do
    sleep 0.5
done

echo "MySQL started"

source venv/bin/activate
flask deploy
exec gunicorn -b :5000 --access-logfile - --error-logfile - application:app

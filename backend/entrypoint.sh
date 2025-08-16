#!/usr/bin/env sh
set -e

python manage.py collectstatic --noinput || true
python manage.py migrate --noinput

exec gunicorn core.wsgi:application --bind 0.0.0.0:${BACKEND_PORT:-8081}

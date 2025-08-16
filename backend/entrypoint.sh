#!/usr/bin/env sh
set -e

python manage.py collectstatic --noinput || true
python manage.py migrate --noinput

# Container's internal port (default 8000)
exec gunicorn core.wsgi:application --bind 0.0.0.0:${BACKEND_PORT:-8000}

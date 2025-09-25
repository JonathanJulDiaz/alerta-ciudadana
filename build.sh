#!/usr/bin/env bash
set -o errexit  # Detiene el script si hay un error

pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
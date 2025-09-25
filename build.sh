#!/usr/bin/env bash
set -o errexit  # Detiene el script si hay un error

pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.com', 'adminpass')" | python manage.py shell

echo "Build complete"
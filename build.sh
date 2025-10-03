#!/usr/bin/env bash
set -o errexit  # Detiene el script si hay un error

# 1. Instalar dependencias de Node.js
npm install

# 2. Compilar Tailwind CSS
npm run build-css

pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# 3. Crear superusuario si no existe (opcional)
echo "from django.contrib.auth.models import User; \
if not User.objects.filter(username='admin').exists(): \
  User.objects.create_superuser('admin', 'admin@email.com', 'adminpass')" \
  | python manage.py shell

echo "✅ Build complete"
#!/usr/bin/env bash
set -o errexit  # Detiene el script si hay un error

# 1. Instalar dependencias de Node.js
npm install

# 2. Compilar Tailwind CSS
npm run build-css

# 3. Migraciones y archivos estáticos
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# 4. Espera breve si estás usando DB externa (opcional)
sleep 2

# 5. Crear superusuario si no existe
python manage.py shell << EOF
from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
password = "adminpass"
email = "admin@email.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
EOF

echo "✅ Build complete"
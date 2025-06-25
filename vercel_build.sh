#!/bin/bash

# Activar entorno virtual (Vercel ya lo hace)
# Instalar dependencias
pip install -r requirements.txt

# Migraciones (opcional pero recomendado si tienes modelos)
python manage.py migrate

# Recolectar archivos estáticos (si usas WhiteNoise o CSS/JS)
python manage.py collectstatic --noinput

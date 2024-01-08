#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar o actualizar pip y otras dependencias de Python
pip install --upgrade pip
pip install uvicorn
#pip install -r requirements.txt

# Navegar al directorio del paquete de tema
cd ./theme/static_src && npm install  && npm run build && npm run dev

# Actualizar e instalar las dependencias de Node.js¿
# Volver al directorio principal del proyecto
cd ../..

# Ejecutar comandos de Django
python ./bin/manage.py migrate
python ./bin/manage.py collectstatic --no-input
python ./bin/manage.py tailwind start

python -m uvicorn  T_Lofi.asgi:application --host 0.0.0.0

# Crear superusuario si se especifica
#if [[ $CREATE_SUPERUSER ]];
#then
#  python ./bin/manage.py createsuperuser --no-input
#fi

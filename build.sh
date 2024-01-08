#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar o actualizar pip y otras dependencias de Python
pip install --upgrade pip
pip install uvicorn
pip install -r requirements.txt

# Navegar al directorio del paquete de tema
cd ./theme/static_src

# Actualizar e instalar las dependencias de Node.js
#npm install -g npm@latest
#npm install  # Esto instala las dependencias según el package.json
npm run dev  # Inicia el entorno de desarrollo de Tailwind CSS

# Volver al directorio principal del proyecto
cd ../..

# Ejecutar comandos de Django
python ./bin/manage.py migrate
python ./bin/manage.py collectstatic --no-input
#python ./bin/manage.py tailwind start

# Crear superusuario si se especifica
if [[ $CREATE_SUPERUSER ]];
then
  python ./bin/manage.py createsuperuser --no-input
fi

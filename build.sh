#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip

pip install uvicorn

pip install -r requirements.txt

# Navega al directorio del paquete de tema
cd ./theme/static_src && npm install

# Ejecuta npm install para instalar las dependencias
npm install


python ./bin/manage.py makemigrations

python ./bin/manage.py migrate

python ./bin/manage.py collectstatic --no-input

python ./bin/manage.py tailwind start


if [[ $CREATE_SUPERUSER ]];
then
  python ./bin/manage.py createsuperuser --no-input
fi
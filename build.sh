#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip

pip install uvicorn

pip install -r requirements.txt

# Navega al directorio del paquete de tema
cd ./theme/static_src && npm install && npm run dev


cd ../..



python ./run_makemigrations.py

python ./run_migrate.py


#Django Migrations and makemigrations

#python ./bin/manage.py makemigrations

python ./bin/manage.py migrate

#python ./bin/manage.py collectstatic --no-input

#python ./bin/manage.py tailwind start


#if [[ $CREATE_SUPERUSER ]];
#then
#  python ./bin/manage.py createsuperuser --no-input
#fi
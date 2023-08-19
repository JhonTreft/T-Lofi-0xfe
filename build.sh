#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip

pip install uvicorn

pip install -r requirements.txt

#npm install

npm install rimraf

npm cache clean --force

npm install tailwind

npm install

python ./bin/manage.py makemigrations

python ./bin/manage.py migrate

python ./bin/manage.py collectstatic --no-input

python ./bin/manage.py tailwind build

python ./bin/manage.py tailwind start


if [[ $CREATE_SUPERUSER ]];
then
  python ./bin/manage.py createsuperuser --no-input
fi
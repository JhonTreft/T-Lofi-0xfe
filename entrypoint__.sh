#!/bin/sh

python bin/manage.py migrate --no-input

if [[ $CREATE_SUPERUSER ]];
then
 python ./bin/manage.py createsuperuser --no-input
fi

python bin/manage.py collectstatic --no-input

gunicorn T_Lofi.wsgi:application --bind 0.0.0.0:8000
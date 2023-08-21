import os
from subprocess import call

# Lista de aplicaciones para las que deseas hacer migraciones
aplicaciones = ['accounts',
                'chat', 'friends','notifications','songs_api']  # Agrega los nombres de tus aplicaciones

for app in aplicaciones:
    call(['python', './bin/manage.py', 'makemigrations', app])

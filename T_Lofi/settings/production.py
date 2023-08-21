
import os

DEBUG = 'RENDER' not in os.environ
#Database Production

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'administration_sc',
        'USER': 'postgresql',
        'PASSWORD': 'dentreaca1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 't_lofi',
        'USER': 'jhon',
        'PASSWORD': 'PHRB0JfcAbIaxWnXRWnyPs2hFfjLbuFb',
        'HOST': 'dpg-cjhu7admrchc73a58qa0-a',
        'PORT': '5432',
    }
}
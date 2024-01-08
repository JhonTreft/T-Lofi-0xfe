from .config_vars import BASE_DIR
import os


#DEBUG = 'RENDER' not in os.environ
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'bd/db.sqlite3',
    }
}
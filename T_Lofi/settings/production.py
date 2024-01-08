
import os

#DEBUG = 'RENDER' not in os.environ
DEBUG = False
#Database Production


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'Eb4aFGB326dFF1fE6515B1*ge6FAGGB4',
        'HOST': 'monorail.proxy.rlwy.net',
        'PORT': '28610',
    }
}

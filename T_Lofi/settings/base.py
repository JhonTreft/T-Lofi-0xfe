from .config_vars  import *
from .local import *
from itertools import chain
#from .production import *

#import cloudinary

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sessions.backends.db',
    
    'django.contrib.staticfiles',
    'django_browser_reload',
    'django.contrib.sites',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    


]





LOCAL_APPS = [
    'apps.chat',
    'apps.songs_api',
    'apps.core',
    'apps.accounts',
    'apps.to_do',
    'apps.notifications',
    'apps.friends'
]


THIRDS_APP = [
    'rest_framework',
    'dotenv',
    'tailwind',
    'theme',
    'fontawesome_5',
    'cloudinary',
    'django_extensions',
    'corsheaders',
    'online_users',
]

INTERNAL_IPS = [
    "127.0.0.1",
    "t-lofi.onrender.com",
]

INSTALLED_APPS  = list(chain(DJANGO_APPS,LOCAL_APPS,THIRDS_APP))

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',


]




AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]






TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




#Cloudinary - Django integtation

cloudinary.config(
    cloud_name="dh0blcdko",
    api_key="329414875762199",
    api_secret="Glf4F_Uyw7RdYmhDWbqyg02jueA",
    
)






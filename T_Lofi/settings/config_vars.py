from dotenv import load_dotenv

from pathlib import Path
from os import path,getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


SECRET_KEY = str(getenv('SECRET_KEY'))


if not(SECRET_KEY):
    exit(1)


ALLOWED_HOSTS = [
    "t-lofi.onrender.com",
    "t-lofi.up.railway.app",
    "localhost",
    "127.0.0.1"
    ".vercel.app"
]

TAILWIND_APP_NAME ='theme'

#NPM_BIN_PATH = 'C:\\Program Files\\nodejs\\npm.cmd'

#NODE_PATH = "C:\\Program Files\\nodejs"

NPM_BIN_PATH = '/usr/bin/npm'

NODE_PATH = '/usr/bin/node'

ROOT_URLCONF = 'T_Lofi.urls'

WSGI_APPLICATION = 'T_Lofi.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = False

USE_TZ = True


#


#Auth django-allauth
SITE_ID = 1

SOCIALACCOUNT_LOGIN_ON_GET=True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'

STATICFILES_DIRS = [
        path.join(BASE_DIR,'static')
    ] # new


MEDIA_URL = 'media/songs/'
MEDIA_ROOT = path.join(BASE_DIR, 'media/songs')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Cloudinary Storage


#Cors
CORS_ORIGIN_ALLOW_ALL = True



#LOGIN REDIRECT
ACCOUNT_LOGIN_TEMPLATE = 'core/user/login.html'

LOGIN_URL = 'login'

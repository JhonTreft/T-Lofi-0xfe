
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'T_Lofi.settings.base')

app = get_wsgi_application()

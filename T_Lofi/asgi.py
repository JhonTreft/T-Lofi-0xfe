

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'T_Lofi.settings.base')

application = get_asgi_application()

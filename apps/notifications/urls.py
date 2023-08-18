from django.urls import path

from .consumers.consumers import NotificationConsumer

from .views import notification_read
urlpatterns = [
    path('notification_read/<int:notificacion_id>',notification_read,name="nt_r"),
    path('ws/notificaciones/', NotificationConsumer.as_asgi()),

]

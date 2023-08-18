from django.shortcuts import render

from .models import Notification
# Create your views here.
def notification_read(request, notificacion_id):
    try:
        notificacion = Notification.objects.get(id=notificacion_id)
        notificacion.read = True
        notificacion.save()
        return 'Success'
    except Notification.DoesNotExist:
        return 'Not found'



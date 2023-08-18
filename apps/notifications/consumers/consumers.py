import json
from channels.generic.websocket import AsyncWebsocketConsumer
from ..models import Notification


from django.shortcuts import render
from django.views.generic import TemplateView
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        await self.channel_layer.group_add(f'user_{self.user.id}', self.channel_name)
        await self.accept()
        await self.send_notifications()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(f'user_{self.user.id}', self.channel_name)

    async def receive(self, text_data):
        pass

    async def send_notifications(self):
        notifications = Notification.objects.filter(user=self.user, read=False)
        notifications_data = []
        for notification in notifications:
            notifications_data.append({
                'id': notification.id,
                'message': notification.message,
                'created_at': notification.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'read': notification.read,
                'type_notification': notification.type_notification,
            })
        await self.send(text_data=json.dumps({
            'notifications': notifications_data
        }))

    async def notification_created(self, event):
        notification = await self.get_notification(event['id'])
        notification_data = {
            'id': notification.id,
            'message': notification.message,
            'created_at': notification.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'read': notification.read,
            'type_notification': notification.type_notification,
        }
        await self.send(text_data=json.dumps({
            'notification': notification_data
        }))

    async def get_notification(self, id):
        return await self.scope['session'].query(Notification).get(id)
    
    
    async def notificar_actualizacion(notificacion):
        channel_layer = get_channel_layer()
        message = {
            "type": "notification.created",
            "id": notificacion.id,
            "message": notificacion.message,
            "created_at": notificacion.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "read": notificacion.read,
            "type_notification": notificacion.type_notification,
        }
        await channel_layer.group_send("notificaciones", message)
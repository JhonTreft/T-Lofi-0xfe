from django.shortcuts import render


from django.views.generic.list import ListView

from .models import ChatAll

from django.core import serializers
from django.http import JsonResponse


from apps.accounts.models import ProfileUserModel

from datetime import datetime, timedelta


from django.views.decorators.csrf import csrf_exempt

import json

from django.utils import timezone

# Protejer Rutas


def ChatView(request):
    # Obtener los chats más recientes
    date_limit = timezone.now() - timedelta(days=7)  # Obtener chats de los últimos 7 días
    chat_all = ChatAll.objects.filter(created_at__gte=date_limit).order_by('-created_at')[:75]

    chat_data = []

    for chat in chat_all:
        # Obtener la URL del avatar para el usuario del mensaje
        user_profile = ProfileUserModel.objects.get(user=chat.user)

        # Crear un diccionario que contenga los datos del mensaje, incluyendo la URL del avatar
        message_data = {
            'username': chat.username,
            'message': chat.message,
            'id': chat.id,
            'avatar': user_profile.avatar.url,
        }

        # Agregar el diccionario al lista de mensajes
        chat_data.append(message_data)

    # Invertir el orden de la lista de mensajes
    chat_data = list(reversed(chat_data))

    return JsonResponse(chat_data, safe=False)



@csrf_exempt
def CreateMessageChatView(request):
    if request.method == 'POST':
        user = request.user
        json_data = json.loads(request.body)
        message = json_data.get('message')
        if message:
            chat_message = ChatAll.objects.create(user=user,message=message,created_at=datetime.now())
            chat_message.save()
            return JsonResponse({'status': 'OK'})
        else:
            return JsonResponse({'status': 'ERROR', 'message': 'No se recibió ningún mensaje.'})
    else:
        return JsonResponse({'status': 'ERROR', 'message': 'La solicitud debe ser un POST.'})
    
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
    try:
        date_limit = timezone.now() - timedelta(days=7)  # Obtener chats de los últimos 7 días
        chat_all = ChatAll.objects.filter(created_at__gte=date_limit).order_by('-created_at')[:75]

        chat_data = []

        for chat in chat_all:
            try:
                # Obtener la URL del avatar para el usuario del mensaje si el perfil existe
                user_profile = ProfileUserModel.objects.get(user=chat.user)
                avatar_url = user_profile.avatar_url
            except ProfileUserModel.DoesNotExist:
                # Si el perfil no existe, establecer la URL del avatar como None o cualquier otro valor por defecto
                continue

            # Crear un diccionario que contenga los datos del mensaje
            message_data = {
                'username': chat.username,
                'message': chat.message,
                'id': chat.id,
                'avatar': avatar_url,
            }

            # Agregar el diccionario a la lista de mensajes
            chat_data.append(message_data)

        # Invertir el orden de la lista de mensajes
        chat_data = list(reversed(chat_data))


        return JsonResponse({'chats':chat_data,'status_code':200}, safe=False,status=200)
    except Exception as e:
        return JsonResponse({'error':str(e),'status_code':400},status=400)


@csrf_exempt
def CreateMessageChatView(request):
    if request.method == 'POST':
        user = request.user
        json_data = json.loads(request.body)
        message = json_data.get('message')
        if message:
            chat_message = ChatAll.objects.create(user=user,message=message,created_at=datetime.now())
            chat_message.save()
            return JsonResponse({'message': 'OK','status_code':200},status=200)
        else:
            return JsonResponse({'status_code': 400, 'message': 'No se recibió ningún mensaje.'},status=400)
    else:
        return JsonResponse({'status_code': 400, 'message': 'La solicitud debe ser un POST.'},status=400)
    
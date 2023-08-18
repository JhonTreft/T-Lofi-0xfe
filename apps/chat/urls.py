from django.urls import path

from .views import ChatView,CreateMessageChatView

urlpatterns = [
    path('chats',ChatView,name="chat"),
    path('chat/create',CreateMessageChatView,name="create_message"),
]

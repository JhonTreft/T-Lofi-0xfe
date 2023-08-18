from django.urls import path
from .views import FriendShipView,send_friend_request,accept_friend_request,reject_friend_request



urlpatterns = [
    #path('friend-requests/', FriendShipView.as_view(), name='friend_requests'),
    path('send_friend_request/<str:user_name>/', send_friend_request, name='send_friend_request'),
    path('friend-requests/<int:request_id>/accept/', accept_friend_request, name='accept_friend_request'),
    path('friend-requests/<int:request_id>/reject/', reject_friend_request, name='reject_friend_request'),
]

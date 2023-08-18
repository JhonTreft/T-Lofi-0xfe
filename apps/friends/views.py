from django.shortcuts import get_object_or_404, render
from django.views import View

from django.http import JsonResponse

from django.db.models import Q

from apps.accounts.models import ProfileUserModel
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FriendRequest,Friendship

from apps.notifications.models import Notification

from django.views import View
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Friendship

from online_users.models import OnlineUserActivity

from django.contrib.auth.models import User


from django.db.models import BooleanField, Case, Value, When
from django.shortcuts import get_object_or_404
from django.utils import timezone


from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist



class FriendShipView(LoginRequiredMixin, View):
    def get(self, request):
        friends = Friendship.objects.filter(Q(user1=request.user) | Q(user2=request.user)).exclude(Q(user1=request.user) & Q(user2=request.user))
        profile_user_friends = []
        
        for friend in friends:
                if friend.user2 == request.user:
                    profile_user_friend = ProfileUserModel.objects.get(user=friend.user1)
                    user_match = User.objects.get(username=friend.user1)
                else:
                    profile_user_friend = ProfileUserModel.objects.get(user=friend.user2)
                    user_match = User.objects.get(username=friend.user2)

                try:
                    online_user_activity = OnlineUserActivity.objects.get(user=user_match)
                    is_user_online = online_user_activity.last_activity >= timezone.now() - timedelta(minutes=15)

                    friend_status = "online" 
                except ObjectDoesNotExist:
                    friend_status = "offline"

                if profile_user_friend:
                    profile_user_friend.status = friend_status
                    profile_user_friends.append(profile_user_friend)

        context = {
            'friends': friends,
            'profile_user_friends': profile_user_friends,
            'count_friends': friends.count()
        }

        return render(request, 'core/friend/friend_requests.html', context)
    


class RespondToFriendRequestView(LoginRequiredMixin, View):
    def post(self, request):
        friend_request_id = request.POST.get('friend_request_id')
        response = request.POST.get('response')
        try:
            friend_request = FriendRequest.objects.get(id=friend_request_id, to_user=request.user)
            if response == 'accept':
                friend_request.accepted = True
                # Realizar las acciones necesarias para aceptar la solicitud
            elif response == 'reject':
                # Realizar las acciones necesarias para rechazar la solicitud
                pass
            friend_request.save()
            return JsonResponse({'success': True})
        except FriendRequest.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Friend request not found'})
        




    



from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import FriendRequest, create_friend_request_notification

@login_required
def send_friend_request(request, user_name):
    from_user = request.user
    to_profile_user = ProfileUserModel.objects.get(user__username=user_name)
    to_user = to_profile_user.user
    message = f'Hola, {to_user.username}, me gustaría ser tu amigo'
    friend_request = FriendRequest.objects.create(from_user=from_user, to_user=to_user, message=message)
    create_friend_request_notification(sender=from_user, receiver=to_user)
    return redirect('profile', user=user_name)





def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    notification_request_friend = get_object_or_404(Notification,id=request_id)

    # Verificar que el usuario actual es el destinatario de la solicitud de amistad
    if request.user != friend_request.to_user:
        return redirect('/') # o cualquier otra página de error que desees mostrar

    # Crear una nueva instancia de Friendship
    Friendship.objects.create(user1=friend_request.from_user, user2=friend_request.to_user)

    # Eliminar la solicitud de amistad
    friend_request.delete()
    
    # Eliminar notificacion de solicitud de amistad
    notification_request_friend.delete()

    return redirect('profile_user')


def reject_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    notification_request_friend = get_object_or_404(Notification,id=request_id)


    # Verificar que el usuario actual es el destinatario de la solicitud de amistad
    if request.user != friend_request.to_user:
        return redirect('/') # o cualquier otra página de error que desees mostrar

    # Eliminar la solicitud de amistad
    friend_request.delete()
    
    # Eliminar notificacion de solicitud de amistad
    notification_request_friend.delete()

    return redirect('profile_user')

    
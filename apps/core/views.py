from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from apps.accounts.models import ProfileUserModel
from online_users.models import OnlineUserActivity


from apps.friends.models import Friendship
from django.contrib.auth.models import User

from django.db.models import Q


from django.utils import timezone

from django.core.exceptions import ObjectDoesNotExist

from datetime import timedelta



@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friends = Friendship.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user)).exclude(Q(user1=self.request.user) & Q(user2=self.request.user))
        profile_user_friends = []
        
        for friend in friends:
                if friend.user2 == self.request.user:
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

        context['friends'] = friends
        context['profile_user_friends'] = profile_user_friends
        context['count_friends'] = friends.count()
     
        return context
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from online_users.models import OnlineUserActivity
from django.db import IntegrityError



@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    try:
        online_user_activity = OnlineUserActivity.objects.get(user=user)
    except OnlineUserActivity.DoesNotExist:
        online_user_activity = OnlineUserActivity.objects.create(user=user,last_activity=timezone.now())
    except IntegrityError as e:
        online_user_activity.last_activity = timezone.now()
        
    online_user_activity.last_activity = timezone.now()
    online_user_activity.save(update_fields=['last_activity'])
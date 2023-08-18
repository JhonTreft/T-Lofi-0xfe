from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from django.views import View
from django.shortcuts import render



from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.utils import timezone



from django.db.models.signals import post_save
from online_users.models import OnlineUserActivity


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    
    update_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    


    def __str__(self):
        return self.message


class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_friends')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_friends')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1.username} - {self.user2.username}"
    
    
    
from apps.notifications.models import Notification

def create_friend_request_notification(sender, receiver):
    message = f'{sender.username} te ha enviado una solicitud de amistad'
    notification = Notification.objects.create(user=receiver, message=message,type_notification="FR")
    


def create_notification(sender,receiver):
    message= f'{sender.message } tal cosa'
    notification = Notification.objects.create(user=receiver, message=message, type_notification="IN")
    
    

    


def create_user_activity(sender, instance, created, **kwargs):
    if created:
        OnlineUserActivity.objects.create(user=instance, last_activity=timezone.now())

post_save.connect(create_user_activity, sender=User)


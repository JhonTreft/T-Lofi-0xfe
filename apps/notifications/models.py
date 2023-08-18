from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Notification(models.Model):
    TYPE_NOTIFICATION=(
        ('friendship','FR'),
        ('messages','MS'),
        ('informative','IN')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    type_notification=models.CharField(max_length=3,blank=True)
    
    
    
    def __str__(self):
        return self.message
    
    
    
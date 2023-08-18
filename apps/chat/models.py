from django.db import models


from django.contrib.auth.models import User

# Create your models here.


class ChatAll(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(max_length=738)
    
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    @property
    def username(self):
        return self.user.username
    
    
    def __str__(self):
        return self.message
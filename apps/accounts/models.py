from django.db import models

from django.contrib.auth.models import User

import cloudinary


# Create your models here.
class ProfileUserModel(models.Model):
    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    BLOQUEADO = 'Bloqueado'

    STATUS_CHOICES = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
        (BLOQUEADO, 'Bloqueado'),
    ]

    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30,blank=True)
    current_job = models.CharField(max_length=200)
    country = models.CharField(max_length=90)
    status_desc = models.CharField(max_length=50)
    description = models.TextField()
    status_user = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVO)
    avatar = models.ImageField(upload_to='users_avatars/',blank=True)
    avatar_url = models.CharField(max_length=1000,blank=True,null=True)
    url_linkedin= models.CharField(max_length=1000,blank=True)
    url_github= models.CharField(max_length=1000,blank=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    update_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    
    
    def save(self, *args, **kwargs):
        if self.avatar:  # Verifica si hay un avatar adjunto
            cloudinary_response = cloudinary.uploader.upload(self.avatar)
            self.avatar_url = cloudinary_response.get('url')  # Guarda la URL de Cloudinary
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'profile'
        verbose_name_plural ='profiles'

    def __str__(self):
        return self.username


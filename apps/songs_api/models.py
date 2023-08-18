from django.db import models

from ..helpers.validation_mp3 import validate_mp3,validate_file_size,validate_image

import cloudinary

from cloudinary.models import CloudinaryField

# Create your models here.


class SongsModel(models.Model):
    title=models.CharField(max_length=90)
    artist=models.CharField(max_length=90)
    description= models.CharField(max_length=50)
    cover_art_url = CloudinaryField('image',blank=True, validators=[validate_image])
    zumba = models.PositiveIntegerField(default=0,blank=True)

    file = models.FileField(validators=[
            validate_mp3,
            validate_file_size,
        ],null=True,blank=True)
    url = models.CharField(max_length=1000, blank=True)
    
    
    class Meta:
        verbose_name='Song'
        verbose_name_plural='Songs'
        
        
    def save(self, *args, **kwargs):
        if self.file and not self.url:  # Si hay un archivo de audio cargado y no hay URL
            self.url = self.file.url  # Asignar la URL generada al campo file_url del objeto SongsModel
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.title
    

    

    
            
        
    
    
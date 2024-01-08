from django.db import models

from ..helpers.validation_mp3 import validate_mp3,validate_file_size,validate_image

import cloudinary.uploader

from cloudinary.models import CloudinaryField
from b2sdk.v1 import B2Api



# Create your models here.
def upload_mp3_file(file_path):
    print(file_path)
    with open(file_path, 'rb') as file:
        upload_result = cloudinary.uploader.upload(file,resource_type='auto')
        return upload_result['url']




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
        if self.file:
                super().save(*args, **kwargs)   
                self.url = upload_mp3_file('./T_Lofi'+self.file.url)
                super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.title
    

    

    
            
        
    
    
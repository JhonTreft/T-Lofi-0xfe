from rest_framework import serializers

from django.contrib.auth.hashers import  make_password

from ..models import SongsModel

from cloudinary.utils import cloudinary_url

class Song_Serializers(serializers.ModelSerializer):
    cover_art_url = serializers.SerializerMethodField()

    class Meta:
        model = SongsModel
        fields= ['id','title','artist','description','cover_art_url','url','zumba']
        
    def get_cover_art_url(self, obj):
        # Obtener la URL completa de la imagen en Cloudinary
        self.cover_art_url = cloudinary_url(obj.cover_art_url.public_id, format=obj.cover_art_url.format, secure=True)[0]
        # Concatenar un string a la URL de la imagen
        return self.cover_art_url
#class SongImageSerializer(CloudinaryFileSerializer):
#   class Meta:
#        model = SongsModel
#        fields = ('image',)
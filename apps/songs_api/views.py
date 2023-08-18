from django.shortcuts import get_object_or_404, render

from .models import SongsModel

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt


from .serializers.serializers import Song_Serializers
from rest_framework.generics import CreateAPIView,ListAPIView
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

class CreateSong(CreateAPIView):
    queryset = SongsModel.objects.all()
    serializer_class =Song_Serializers


    
class ListSongs(ListAPIView):
    queryset= SongsModel.objects.all()
    serializer_class = Song_Serializers


@csrf_exempt
def ZumbaSong(request):
    if request.method == 'POST' and request.is_ajax():
        cancion_id = request.POST.get('id')
        is_saved = request.POST.get('saved') == 'true'
        
        # Aquí debes agregar la lógica para guardar o desguardar la canción
        # utilizando los valores "cancion_id" e "is_saved"
        
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=400)
    
    
@csrf_exempt
def increment_zumba(request, id):
    if(request.method =="POST"):
        print("desde el song",id)
        # Obtener el objeto correspondiente al ID
        song = get_object_or_404(SongsModel, id=id)
        
        # Actualizar el campo que desee
        song.zumba += 1
        song.save()
        
        # Devolver una respuesta JSON indicando que la operación se completó correctamente
        return JsonResponse({'mensaje': 'Campo incrementado correctamente'})
    
    return JsonResponse({'mensaje': 'Peticion GET no valida'})




@csrf_exempt
def not_song(request, id):
    if(request.method =="POST"):
        print("desde el song",id)
        # Obtener el objeto correspondiente al ID
        song = get_object_or_404(SongsModel, id=id)
        
        # Actualizar el campo que desee
        song.zumba -= 1
        song.save()
        
        # Devolver una respuesta JSON indicando que la operación se completó correctamente
        return JsonResponse({'mensaje': 'no gustar correctamente'})
    
    return JsonResponse({'mensaje': 'Peticion GET no valida'})
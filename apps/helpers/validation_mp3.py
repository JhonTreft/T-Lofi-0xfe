from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _
from PIL import Image


def validate_mp3(value):
    if not value.name.endswith('.mp3'):
        raise ValidationError('Solo se permiten archivos MP3.')



def validate_file_size(value):
    filesize= value.size
    
    if filesize > 10 * 1024 * 1024:  # 10 MB en bytes
        raise ValidationError(("El tamaño del archivo no puede ser superior a 10 MB."))
    

def validate_image(image):
    """
    Valida que el archivo sea una imagen válida.
    """
    try:
        # Abre el archivo de imagen utilizando Pillow
        with Image.open(image) as img:
            # Comprueba si el archivo es un formato de imagen válido
            if img.format not in ['JPEG', 'PNG', 'GIF','JPG']:
                raise ValidationError(
                    _("Formato de imagen no válido. Los formatos válidos son JPEG, PNG y GIF."),
                    code='invalid_image'
                )
    except Exception as e:
        raise ValidationError(
            _("No se pudo leer la imagen. Asegúrate de que el archivo sea una imagen válida."),
            code='invalid_image'
        )
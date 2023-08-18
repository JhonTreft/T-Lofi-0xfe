from django.urls import path

from .views import CreateSong,ListSongs,increment_zumba,not_song

urlpatterns = [
    path('song', CreateSong.as_view(),name="create song"),
    path('songs', ListSongs.as_view(),name="list songs"),
    path('increment_zumba/<int:id>', increment_zumba, name='increment_zumba'),
    path('not_song/<int:id>',not_song,name="no_song"),
]
    
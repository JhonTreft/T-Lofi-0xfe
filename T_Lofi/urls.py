
from django.contrib import admin
from django.urls import path,include




from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.core.urls')),
    path('api/',include('apps.songs_api.urls')),
    path('account/',include('apps.accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('',include('apps.friends.urls')),
    path('',include('apps.notifications.urls')),
    #path(r'^status/', include('online.urls')),
    path('',include('apps.chat.urls'))


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path('media/<path>', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
    
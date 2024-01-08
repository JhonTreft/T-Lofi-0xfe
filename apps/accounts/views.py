from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import TemplateView

from django.views.generic.edit import View

from django.contrib.auth.models import User

from django.urls import reverse

from .models import ProfileUserModel

from django.contrib import messages

from apps.notifications.models import Notification

from django.db.models import Q


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from online_users.models import OnlineUserActivity



from apps.friends.models import FriendRequest,Friendship

class LoginView(TemplateView):
    template_name = "core/user/login.html"
    
    

    
    
    
class SettingAccountView(TemplateView):
    template_name = 'core/user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el usuario autenticado
        user = self.request.user
        
        try:
            user_unique = ProfileUserModel.objects.get(user=user)
        except ProfileUserModel.DoesNotExist:
                user_unique = None
                

        
        
        context['user_raid'] = user_unique
        context['user'] = user
       
        
        user_notification = Notification.objects.filter(user=self.request.user).exists()
        if user_notification:
            
            context['notifications'] = Notification.objects.filter(user=self.request.user)
            context['notifications_count'] = Notification.objects.filter(user=self.request.user,read=False).count()
        
        
        context['friends_count'] = Friendship.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user)).count()
        
            

        
        
        return context
    

class CreateProfileUserView(View):
    def get(self, request):
        return render(request, 'core/user/create_profile.html')

    def post(self, request):
        model = ProfileUserModel
        user_= request.user
        
        # Validación de campos antes de asignar valores
        username = request.POST.get('username')
        current_job = request.POST.get('current_job')
        country = request.POST.get('country')
        status_desc = request.POST.get('status_desc')
        description = request.POST.get('description')
        avatar = request.FILES.get('avatar')
        url_linkedin = request.POST.get('linkedin')
        url_github = request.POST.get('github')

        # Verificación de campos no vacíos
        if not all([username, current_job, country, status_desc, description, avatar, url_linkedin, url_github]):
            # Si alguno de los campos está vacío, manejar el error, redirigir o responder adecuadamente
            # Por ejemplo, puedes retornar un mensaje de error o redirigir a una página de error
            messages.warning(request, 'Debes de llenar todos los campos y avatar para poder continuar🤡🤡')
        else:
            if not(model.objects.filter(user=user_).exists()):
                create_profile = model.objects.create(
                user = request.user,
                username=request.POST.get('username'),
                current_job=request.POST.get('current_job'),
                country=request.POST.get('country'),
                status_desc=request.POST.get('status_desc'),
                description=request.POST.get('description'),
                avatar=request.FILES.get('avatar'),
                url_linkedin=request.POST.get('linkedin'),
                url_github=request.POST.get('github')
                )
                
                create_profile.save()
                messages.success(request, 'La acción se ha completado con éxito.')
                return HttpResponseRedirect(reverse('profile_user'))
            
            
            messages.success(request, 'Ya existe un perfil para este usuario')
            return HttpResponseRedirect(reverse('create_profile'))
        
        return HttpResponseRedirect(reverse('create_profile'))


class UserProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ProfileUserModel
    template_name = 'user_profile.html'
    context_object_name = 'profile'

    def test_func(self):
        # Verifica si el usuario actual es el propietario del perfil o si es un superusuario
        profile_user = self.get_object().user
        return self.request.user == profile_user or self.request.user.is_superuser
    
    

def ProfileView(request, user):
    # Obtener el objeto User correspondiente al nombre de usuario
    user_obj = get_object_or_404(User, username=user)

    # Obtener el objeto ProfileUserModel correspondiente al objeto User
    context = {}

    user_request = request.user
    profile_user_obj = get_object_or_404(ProfileUserModel, user=user_obj)


    # Verificar si los usuarios son amigos
    is_friend1 = False
    is_friend2 = False
    try:
        friendship = Friendship.objects.get(user1=user_obj, user2=user_request)
        is_friend1 = True
        
    except Friendship.DoesNotExist:
        pass
    
    
    try:
        friendship = Friendship.objects.get(user1=user_request, user2=user_obj)
        is_friend2 = True
        
    except Friendship.DoesNotExist:
        pass
    
    
    

    # Verificar si hay solicitudes de amistad pendientes (si los usuarios no son amigos)
    has_sent_request_to_user = False
    has_received_request_from_user = False
    if not is_friend1 or is_friend2:
        sent_requests = FriendRequest.objects.filter(from_user=user_request, accepted=False, to_user=user_obj)
        received_requests = FriendRequest.objects.filter(from_user=user_obj, accepted=False, to_user=user_request)
        has_sent_request_to_user = sent_requests.exists()
        has_received_request_from_user = received_requests.exists()
        
        context['sent_requests'] = sent_requests
        context['received_requests'] = received_requests
        context['has_sent_request_to_user'] = has_sent_request_to_user
        context['has_received_request_from_user'] = has_received_request_from_user
    

    context['user_raid'] = profile_user_obj
    context['user'] = user
    
    context['is_friend1'] = is_friend1
    context['is_friend2'] = is_friend2
    
    
    context['friends_count'] = Friendship.objects.filter(Q(user2=user_obj) | Q(user1=user_obj)).count()

    
    
    
    return render(request, 'core/user/profile.html', context)


from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    # Eliminar la información de seguimiento de actividad del usuario
    user_delete_activity= OnlineUserActivity.objects.get(user=request.user)
    user_delete_activity.delete()
    
    # Cerrar la sesión del usuario
    logout(request)
    # Redirigir al usuario a la página de inicio de sesión
    return redirect('login')
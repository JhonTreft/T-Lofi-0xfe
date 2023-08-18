from django.urls import path
from .views import LoginView,SettingAccountView,CreateProfileUserView,UserProfileDetailView,ProfileView,logout_view

urlpatterns = [
   path('login', LoginView.as_view(),name="login"),
   path('profile',SettingAccountView.as_view(),name="profile_user"),
   path('crear-perfil/', CreateProfileUserView.as_view(), name='create_profile'),
   path('profile/<str:user>/', ProfileView, name='profile'),
   path('logout',logout_view,name="logout")


]

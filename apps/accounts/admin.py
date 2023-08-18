from django.contrib import admin

from .models import ProfileUserModel
# Register your models here.

from .apps import AccountsConfig


@admin.register(ProfileUserModel)
class ProfileUserAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin

from .models import FriendRequest,Friendship
# Register your models here.

@admin.register(FriendRequest)
class FriendsAdmin(admin.ModelAdmin):
    pass


@admin.register(Friendship)
class FriendShipAdmin(admin.ModelAdmin):
    pass
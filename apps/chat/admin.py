from django.contrib import admin


from .models import ChatAll
# Register your models here.

@admin.register(ChatAll)
class ChatAdmin(admin.ModelAdmin):
    pass
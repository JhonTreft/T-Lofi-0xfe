from django.contrib import admin


from .models import Notification
# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    fields = ('id','user','message','created_at')

from django.contrib import admin
from .models import Message
from django.contrib.auth.models import Group


# Register your models here.

admin.site.site_header = 'administration Bamba'

class MessageAdmins(admin.ModelAdmin):
	
	list_display = ('nomPrenom','Email', 'sujet', 'message')
	list_filter = ('date',)

admin.site.register(Message, MessageAdmins)


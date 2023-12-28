from django.contrib import admin
from .models import *

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('pk','user', 'name')


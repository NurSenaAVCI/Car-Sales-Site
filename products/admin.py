from django.contrib import admin
from .models import *

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('pk','name')

@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ('pk','title')

admin.site.register(Bag)

@admin.register(BagItem)
class BagItemAdmin(admin.ModelAdmin):
    list_display = ('product',)

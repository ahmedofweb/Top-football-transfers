from django.contrib import admin
from .models import *

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'country']
    list_editable = ['logo']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'club']

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['player', 'after_club', 'before_club']

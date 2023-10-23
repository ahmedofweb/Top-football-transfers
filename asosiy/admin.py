from django.contrib import admin
from .models import *

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'country']
    list_editable = ['logo']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'club', 'cost', 'country', 'dob']
    list_editable = ['cost']

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['player', 'before_club', 'after_club', 'selling_cost']
    list_editable = ['selling_cost']
@admin.register(PresentSeason)
class PresentSeasonAdmin(admin.ModelAdmin):
    list_display = ['p_season']

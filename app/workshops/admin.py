from django.contrib import admin
from .models import Registration, Workshop

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', "location")
    search_fields = ('title', "location")
    list_filter = ('start_date',)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('workshop', 'name', 'email', 'created_at')
    search_fields = ('workshop__title', 'name', 'email')
    list_filter = ('workshop',)
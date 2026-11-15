from django.contrib import admin
from .models import Habitacion

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = (
        'numero',
        'tipo',
        'precio_noche',
        'capacidad',
        'disponible'
    )

    list_filter = ('tipo', 'disponible')
    search_fields = ('numero',)
    ordering = ('numero',)
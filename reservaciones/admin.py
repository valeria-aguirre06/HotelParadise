from django.contrib import admin
from .models import Reservacion


@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cliente',
        'habitacion',
        'fecha_entrada',
        'fecha_salida',
        'total',
        'estado'
    )

    list_filter = ('estado', 'fecha_entrada')
    search_fields = (
        'cliente__nombre',
        'cliente__apellidos',
        'habitacion__numero'
    )
    ordering = ('-fecha_entrada',)
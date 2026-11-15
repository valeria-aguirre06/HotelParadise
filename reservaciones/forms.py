from django import forms
from .models import Reservacion


class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion

        fields = [
            'cliente',
            'habitacion',
            'fecha_entrada',
            'fecha_salida',
            'estado'
        ]

        labels = {
            'cliente': 'Cliente',
            'habitacion': 'Habitación',
            'fecha_entrada': 'Fecha de entrada',
            'fecha_salida': 'Fecha de salida',
            'estado': 'Estado de la reservación'
        }

        widgets = {
            'fecha_entrada': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'fecha_salida': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
        }
from django.db import models
from django.core.exceptions import ValidationError
from clientes.models import Cliente
from habitaciones.models import Habitacion


class Reservacion(models.Model):
    ESTADOS = [
        ('Activa', 'Activa'),
        ('Cancelada', 'Cancelada'),
        ('Finalizada', 'Finalizada'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='reservaciones'
    )

    habitacion = models.ForeignKey(
        Habitacion,
        on_delete=models.PROTECT,
        related_name='reservaciones'
    )

    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    estado = models.CharField(
        max_length=12,
        choices=ESTADOS,
        default='Activa'
    )

    class Meta:
        verbose_name = "Reservación"
        verbose_name_plural = "Reservaciones"

    def _str_(self):
        return f"Reservación {self.id} - {self.cliente}"

    def clean(self):
        super().clean()

        if self.fecha_entrada and self.fecha_salida:

            # Validar que la salida sea posterior a la entrada
            if self.fecha_salida <= self.fecha_entrada:
                raise ValidationError({
                    'fecha_salida': 'La fecha de salida debe ser posterior a la fecha de entrada.'
                })

            if self.habitacion_id:

                # Comprobar que la habitacion este disponible
                if self.estado == 'Activa' and not self.habitacion.disponible:
                    raise ValidationError({
                        'habitacion': 'Esta habitacion no esta disponible.'
                    })

                # Evitar reservaciones con fechas que se encimen
                if self.estado != 'Cancelada':
                    reservaciones_existentes = Reservacion.objects.filter(
                        habitacion=self.habitacion,
                        fecha_entrada__lt=self.fecha_salida,
                        fecha_salida__gt=self.fecha_entrada
                    ).exclude(estado='Cancelada')

                    if self.pk:
                        reservaciones_existentes = reservaciones_existentes.exclude(
                            pk=self.pk
                        )

                    if reservaciones_existentes.exists():
                        raise ValidationError({
                            'habitacion': 'La habitacion ya tiene una reservacion en esas fechas.'
                        })

                # Calcular el precio total
                noches = (self.fecha_salida - self.fecha_entrada).days
                self.total = noches * self.habitacion.precio_noche

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
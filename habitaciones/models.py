from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class Habitacion(models.Model):
    TIPOS = [
        ('Individual', 'Individual'),
        ('Doble', 'Doble'),
        ('Suite', 'Suite'),
        ('Presidencial', 'Presidencial'),
    ]

    numero = models.PositiveIntegerField(unique=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    precio_noche = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    capacidad = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(
        upload_to='habitaciones/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"
        
    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo}"
from decimal import Decimal
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from clientes.models import Cliente
from habitaciones.models import Habitacion
from reservaciones.models import Reservacion

@login_required(login_url='login')
def dashboard(request):
    total_clientes = Cliente.objects.count()
    total_habitaciones = Habitacion.objects.count()
    habitaciones_disponibles = Habitacion.objects.filter(
        disponible=True
    ).count()

    total_reservaciones = Reservacion.objects.count()

    reservaciones_validas = Reservacion.objects.exclude(
        estado='Cancelada'
    )

    total_reservado = reservaciones_validas.aggregate(
        total=Sum('total')
    )['total'] or Decimal('0.00')

    contexto = {
        'total_clientes': total_clientes,
        'total_habitaciones': total_habitaciones,
        'habitaciones_disponibles': habitaciones_disponibles,
        'total_reservaciones': total_reservaciones,
        'total_reservado': total_reservado,
    }

    return render(request, 'core/dashboard.html', contexto)

# Reportes del hotel
@login_required(login_url='login')
def reportes(request):

    # Cantidad de reservaciones por estado
    reservaciones_activas = Reservacion.objects.filter(
        estado='Activa'
    ).count()

    reservaciones_canceladas = Reservacion.objects.filter(
        estado='Cancelada'
    ).count()

    reservaciones_finalizadas = Reservacion.objects.filter(
        estado='Finalizada'
    ).count()

    # Total de reservaciones no canceladas
    total_reservado = Reservacion.objects.exclude(
        estado='Cancelada'
    ).aggregate(
        total=Sum('total')
    )['total'] or Decimal('0.00')

    # Consultar el historial de reservaciones
    lista_reservaciones = Reservacion.objects.select_related(
        'cliente', 'habitacion'
    ).order_by('-fecha_entrada')

    contexto = {
        'reservaciones_activas': reservaciones_activas,
        'reservaciones_canceladas': reservaciones_canceladas,
        'reservaciones_finalizadas': reservaciones_finalizadas,
        'total_reservado': total_reservado,
        'reservaciones': lista_reservaciones,
    }

    return render(request, 'core/reportes.html', contexto)
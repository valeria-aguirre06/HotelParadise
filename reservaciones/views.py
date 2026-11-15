from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Reservacion
from .forms import ReservacionForm


# Consultar las reservaciones
@login_required(login_url='login')
def lista_reservaciones(request):
    reservaciones = Reservacion.objects.select_related(
        'cliente', 'habitacion'
    ).order_by('-fecha_entrada')

    return render(request, 'reservaciones/lista.html', {
        'reservaciones': reservaciones
    })


# Registrar una reservacion
@login_required(login_url='login')
def crear_reservacion(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_reservaciones')
    else:
        form = ReservacionForm()

    return render(request, 'reservaciones/formulario.html', {
        'form': form,
        'titulo': 'Registrar reservación'
    })


# Modificar una reservacion
@login_required(login_url='login')
def editar_reservacion(request, id):
    reservacion = get_object_or_404(Reservacion, id=id)

    if request.method == 'POST':
        form = ReservacionForm(
            request.POST,
            instance=reservacion
        )

        if form.is_valid():
            form.save()
            return redirect('lista_reservaciones')
    else:
        form = ReservacionForm(instance=reservacion)

    return render(request, 'reservaciones/formulario.html', {
        'form': form,
        'titulo': 'Modificar reservación'
    })


# Cancelar una reservacion
@login_required(login_url='login')
def cancelar_reservacion(request, id):
    reservacion = get_object_or_404(Reservacion, id=id)

    if request.method == 'POST':
        reservacion.estado = 'Cancelada'
        reservacion.save()
        return redirect('lista_reservaciones')

    return render(request, 'reservaciones/cancelar.html', {
        'reservacion': reservacion
    })
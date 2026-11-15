from django.shortcuts import render, redirect, get_object_or_404
from .models import Habitacion
from .forms import HabitacionForm
from django.contrib.auth.decorators import login_required

# Consultar habitaciones
@login_required(login_url='login')
def lista_habitaciones(request):
    habitaciones = Habitacion.objects.all().order_by('numero')

    return render(
        request,
        'habitaciones/lista.html',
        {'habitaciones': habitaciones}
    )


# Registrar habitación
@login_required(login_url='login')
def crear_habitacion(request):
    form = HabitacionForm(
        request.POST or None,
        request.FILES or None
    )

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('lista_habitaciones')

    return render(
        request,
        'habitaciones/formulario.html',
        {'form': form}
    )


# Modificar habitación
@login_required(login_url='login')
def editar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)

    form = HabitacionForm(
        request.POST or None,
        request.FILES or None,
        instance=habitacion
    )

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('lista_habitaciones')

    return render(
        request,
        'habitaciones/formulario.html',
        {'form': form}
    )


# Eliminar habitación
@login_required(login_url='login')
def eliminar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)

    if request.method == 'POST':

        # Impedir eliminar habitaciones con reservaciones activas
        if habitacion.reservaciones.filter(estado='Activa').exists():
            return render(request, 'habitaciones/eliminar.html', {
                'habitacion': habitacion,
                'error': 'No se puede eliminar esta habitación porque tiene reservaciones activas.'
            })

        # Conservar el historial de reservaciones canceladas o finalizadas
        if habitacion.reservaciones.exists():
            return render(request, 'habitaciones/eliminar.html', {
                'habitacion': habitacion,
                'error': 'No se puede eliminar esta habitación porque tiene un historial de reservaciones.'
            })

        habitacion.delete()
        return redirect('lista_habitaciones')

    return render(request, 'habitaciones/eliminar.html', {
        'habitacion': habitacion
    })
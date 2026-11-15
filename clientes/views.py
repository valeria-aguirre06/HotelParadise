from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required

# Consultar y buscar clientes
@login_required(login_url='login')
def lista_clientes(request):
    busqueda = request.GET.get('q', '')
    clientes = Cliente.objects.all().order_by('nombre')

    if busqueda:
        clientes = clientes.filter(
            Q(nombre__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(correo__icontains=busqueda)
        )

    return render(request, 'clientes/lista.html', {
        'clientes': clientes,
        'busqueda': busqueda
    })


# Registrar clientes
@login_required(login_url='login')
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'clientes/formulario.html', {
        'form': form,
        'titulo': 'Registrar cliente'
    })


# Modificar clientes
@login_required(login_url='login')
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/formulario.html', {
        'form': form,
        'titulo': 'Modificar cliente'
    })


# Eliminar clientes
@login_required(login_url='login')
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')

    return render(request, 'clientes/eliminar.html', {
        'cliente': cliente
    })
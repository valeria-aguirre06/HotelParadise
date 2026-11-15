from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Clientes
    path('', views.lista_clientes, name='lista_clientes'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),

    # Inicio y cierre de sesión
    path(
        'login/',
        LoginView.as_view(
            template_name='clientes/login.html',
            next_page='lista_clientes'
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(next_page='login'),
        name='logout'
    ),
]
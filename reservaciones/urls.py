from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_reservaciones, name='lista_reservaciones'),
    path('crear/', views.crear_reservacion, name='crear_reservacion'),
    path('editar/<int:id>/', views.editar_reservacion, name='editar_reservacion'),
    path('cancelar/<int:id>/', views.cancelar_reservacion, name='cancelar_reservacion'),
]
# Hotel Paradise
Sistema de reservación de hotel desarrollado con Django.

## Requisitos
- Python
- Django
- Pillow
- SQLite

## Instalación
1. Descargar el proyecto desde GitHub.
2. Abrir CMD dentro de la carpeta HotelParadise.
3. Crear el entorno virtual:

python -m venv venv

4. Activar el entorno virtual:

venv\Scripts\activate

5. Instalar las dependencias:

pip install -r requirements.txt

6. Aplicar las migraciones:

python manage.py migrate

7. Crear un usuario administrador:

python manage.py createsuperuser

8. Ejecutar el servidor:

python manage.py runserver

## Acceso
Panel administrativo:
http://127.0.0.1:8000/admin/

Habitaciones:
http://127.0.0.1:8000/habitaciones/
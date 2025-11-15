from django.urls import path
from . import views

app_name = "app_habitacion"

urlpatterns = [
	path("", views.listar_habitaciones, name="listar_habitaciones"),
	path("crear/", views.crear_habitacion, name="crear_habitacion"),
	path("editar/<int:id>/", views.editar_habitacion, name="editar_habitacion"),
	path("eliminar/<int:id>/", views.eliminar_habitacion, name="eliminar_habitacion"),
]

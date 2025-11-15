from django.urls import path
from . import views

app_name = "app_medico"

urlpatterns = [
	path("", views.listar_medicos, name="listar_medicos"),
	path("crear/", views.crear_medico, name="crear_medico"),
	path("editar/<int:id>/", views.editar_medico, name="editar_medico"),
	path("eliminar/<int:id>/", views.eliminar_medico, name="eliminar_medico"),
]

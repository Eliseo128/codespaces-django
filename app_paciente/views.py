from django.shortcuts import render, redirect, get_object_or_404
from django import forms

from .models import Paciente


class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = [
			"nombre",
			"apellido",
			"fecha_nacimiento",
			"genero",
			"direccion",
			"telefono",
			"email",
			"num_seguro_social",
		]
		widgets = {
			"fecha_nacimiento": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
			"genero": forms.Select(attrs={"class": "form-select"}),
			"nombre": forms.TextInput(attrs={"class": "form-control"}),
			"apellido": forms.TextInput(attrs={"class": "form-control"}),
			"direccion": forms.TextInput(attrs={"class": "form-control"}),
			"telefono": forms.TextInput(attrs={"class": "form-control"}),
			"email": forms.EmailInput(attrs={"class": "form-control"}),
			"num_seguro_social": forms.TextInput(attrs={"class": "form-control"}),
		}


def listar_pacientes(request):
	pacientes = Paciente.objects.all().order_by("apellido", "nombre")
	return render(request, "app_paciente/ver_pacientes.html", {"pacientes": pacientes})


def crear_paciente(request):
	if request.method == "POST":
		form = PacienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("app_paciente:listar_pacientes")
	else:
		form = PacienteForm()
	return render(request, "app_paciente/crear_paciente.html", {"form": form})


def editar_paciente(request, id):
	paciente = get_object_or_404(Paciente, id_paciente=id)
	if request.method == "POST":
		form = PacienteForm(request.POST, instance=paciente)
		if form.is_valid():
			form.save()
			return redirect("app_paciente:listar_pacientes")
	else:
		form = PacienteForm(instance=paciente)
	return render(request, "app_paciente/actuelizar_paciente.html", {"form": form, "paciente": paciente})


def eliminar_paciente(request, id):
	paciente = get_object_or_404(Paciente, id_paciente=id)
	if request.method == "POST":
		paciente.delete()
		return redirect("app_paciente:listar_pacientes")
	return render(request, "app_paciente/guardar_actualizar_paciente.html", {"paciente": paciente})

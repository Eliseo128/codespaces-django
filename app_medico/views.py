from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Medico

class MedicoForm(forms.ModelForm):
	class Meta:
		model = Medico
		fields = [
			"nombre", "apellido", "especialidad", "telefono", "email",
			"licencia_medica", "salario", "fecha_contratacion"
		]
		widgets = {
			"nombre": forms.TextInput(attrs={"class": "form-control"}),
			"apellido": forms.TextInput(attrs={"class": "form-control"}),
			"especialidad": forms.TextInput(attrs={"class": "form-control"}),
			"telefono": forms.TextInput(attrs={"class": "form-control"}),
			"email": forms.EmailInput(attrs={"class": "form-control"}),
			"licencia_medica": forms.TextInput(attrs={"class": "form-control"}),
			"salario": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
			"fecha_contratacion": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
		}

def listar_medicos(request):
	medicos = Medico.objects.all().order_by("apellido", "nombre")
	return render(request, "app_medico/ver_medico.html", {"medicos": medicos})

def crear_medico(request):
	if request.method == "POST":
		form = MedicoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("app_medico:listar_medicos")
	else:
		form = MedicoForm()
	return render(request, "app_medico/crear_medico.html", {"form": form})

def editar_medico(request, id):
	medico = get_object_or_404(Medico, id_medico=id)
	if request.method == "POST":
		form = MedicoForm(request.POST, instance=medico)
		if form.is_valid():
			form.save()
			return redirect("app_medico:listar_medicos")
	else:
		form = MedicoForm(instance=medico)
	return render(request, "app_medico/actualizar_medico.html", {"form": form, "medico": medico})

def eliminar_medico(request, id):
	medico = get_object_or_404(Medico, id_medico=id)
	if request.method == "POST":
		medico.delete()
		return redirect("app_medico:listar_medicos")
	return render(request, "app_medico/eliminar_medico.html", {"medico": medico})

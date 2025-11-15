from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Habitacion

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ["numero_habitacion", "tipo_habitacion", "estado_habitacion", "costo_diario", "capacidad", "descripcion"]
        widgets = {
            "numero_habitacion": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_habitacion": forms.Select(attrs={"class": "form-select"}),
            "estado_habitacion": forms.Select(attrs={"class": "form-select"}),
            "costo_diario": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "capacidad": forms.NumberInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

def listar_habitaciones(request):
    habitaciones = Habitacion.objects.all().order_by("numero_habitacion")
    return render(request, "app_habitacion/ver_habitacion.html", {"habitaciones": habitaciones})

def crear_habitacion(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_habitacion:listar_habitaciones")
    else:
        form = HabitacionForm()
    return render(request, "app_habitacion/crear_habitacion.html", {"form": form})

def editar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id_habitacion=id)
    if request.method == "POST":
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect("app_habitacion:listar_habitaciones")
    else:
        form = HabitacionForm(instance=habitacion)
    return render(request, "app_habitacion/actualizar_habitacion.html", {"form": form, "habitacion": habitacion})

def eliminar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id_habitacion=id)
    if request.method == "POST":
        habitacion.delete()
        return redirect("app_habitacion:listar_habitaciones")
    return render(request, "app_habitacion/eliminar_habitacion.html", {"habitacion": habitacion})

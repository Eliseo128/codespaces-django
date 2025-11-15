
# Hospital Siglo 21 — Sistema de Administración

Este proyecto es un sistema web para la administración hospitalaria, desarrollado con Django y Bootstrap. Permite gestionar pacientes, médicos y habitaciones de manera sencilla y elegante.

## Características
- CRUD de pacientes, médicos y habitaciones
- Interfaz moderna y responsiva
- Navegación intuitiva
- Colores diferenciados por módulo

## Instalación
1. Clona el repositorio:

## Estructura de Carpetas y Archivos

```
db.sqlite3
manage.py
README.md
requirements.txt
app_habitacion/
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	urls.py
	views.py
	migrations/
		__init__.py
		0001_initial.py
	templates/
		app_habitacion/
			actualizar_habitacion.html
			crear_habitacion.html
			eliminar_habitacion.html
			ver_habitacion.html
app_medico/
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	urls.py
	views.py
	migrations/
		__init__.py
		0001_initial.py
	templates/
		app_medico/
			actualizar_medico.html
			crear_medico.html
			eliminar_medico.html
			ver_medico.html
app_paciente/
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	urls.py
	views.py
	migrations/
		__init__.py
		0001_initial.py
	templates/
		app_paciente/
			actuelizar_paciente.html
			crear_paciente.html
			guardar_actualizar_paciente.html
			ver_pacientes.html
backend_oxxo/
	__init__.py
	asgi.py
	settings.py
	urls.py
	wsgi.py
	core/
		views.py
	static/
		main.css
	templates/
		index.html
templates/
	base.html
	footer.html
	header.html
	inicio.html
	navbar.html
```

---

## Pasos para crear el proyecto

### 1. Crear el entorno y el proyecto Django
```bash
python -m venv venv
source venv/bin/activate
pip install django
django-admin startproject backend_oxxo .
```

### 2. Crear las aplicaciones
```bash
python manage.py startapp app_paciente
python manage.py startapp app_medico
python manage.py startapp app_habitacion
```

### 3. Configurar settings.py
- Agregar las apps a `INSTALLED_APPS`.
- Configurar rutas de templates y archivos estáticos.

### 4. Definir los modelos
- Crear los modelos en cada app (`models.py`) según los requerimientos de pacientes, médicos y habitaciones.

### 5. Realizar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear las vistas y URLs
- Implementar vistas CRUD en cada app (`views.py`).
- Definir rutas en `urls.py` de cada app y agregarlas al `urls.py` principal.

### 7. Crear las plantillas HTML
- Usar Bootstrap y colores diferenciados para cada módulo.
- Personalizar formularios y navegación.

### 8. Probar el servidor
```bash
python manage.py runserver
```

### 9. Inicializar repositorio Git y subir a GitHub
```bash
git init
git add .
git commit -m "Primer commit"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
```

---

## Autor
Ing. Eliseo Nava

---

Este README resume la estructura y los pasos principales para crear, configurar y publicar el sistema de administración hospitalaria Siglo 21 en GitHub.

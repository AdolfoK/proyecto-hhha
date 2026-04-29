from django.contrib import admin
from .models import Paciente, Examen

# Registramos los modelos para que aparezcan en el panel /admin
admin.site.register(Paciente)
admin.site.register(Examen)
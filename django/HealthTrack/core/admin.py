from django.contrib import admin
from .models import Paciente
# Register your models here.

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'cep', 'endereco')
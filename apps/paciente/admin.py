from django.contrib import admin

from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'nome', 'cpf', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'cpf')
    ordering = ('nome',)

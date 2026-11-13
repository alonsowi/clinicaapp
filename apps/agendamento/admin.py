from django.contrib import admin

from .models import Agendamento


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('id_agendamento', 'chamado', 'data', 'horario', 'id_paciente', 'id_recep')
    list_filter = ('data', 'id_recep')
    search_fields = ('chamado', 'id_paciente__nome')
    date_hierarchy = 'data'
    ordering = ('-data', 'horario')

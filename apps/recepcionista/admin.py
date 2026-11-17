from django.contrib import admin

from .models import Recepcionista


@admin.register(Recepcionista)
class RecepcionistaAdmin(admin.ModelAdmin):
    list_display = ('id_recep', 'nome', 'cpf', 'telefone', 'turno')
    list_filter = ('turno',)
    search_fields = ('nome', 'cpf')
    ordering = ('nome',)

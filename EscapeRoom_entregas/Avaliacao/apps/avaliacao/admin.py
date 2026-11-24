from django.contrib import admin

from .models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nota', 'recomendaria', 'cliente', 'sessao', 'criada_em')
    list_filter = ('recomendaria', 'nota')
    search_fields = ('comentario',)
    ordering = ('-criada_em',)

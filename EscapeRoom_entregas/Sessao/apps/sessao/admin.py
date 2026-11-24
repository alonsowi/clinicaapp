from django.contrib import admin

from .models import Sessao


@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'status', 'resultado', 'pontuacao_final', 'inicio_real')
    list_filter = ('status', 'resultado')
    search_fields = ('codigo',)
    ordering = ('codigo',)

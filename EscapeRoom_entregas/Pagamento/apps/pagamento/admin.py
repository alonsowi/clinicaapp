from django.contrib import admin

from .models import Pagamento


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo_transacao', 'valor', 'metodo', 'status', 'agendamento')
    list_filter = ('status', 'metodo')
    search_fields = ('codigo_transacao',)
    ordering = ('codigo_transacao',)

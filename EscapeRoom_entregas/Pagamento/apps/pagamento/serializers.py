from rest_framework import serializers

from .models import Pagamento


class PagamentoSerializer(serializers.ModelSerializer):
    metodo_display = serializers.CharField(source='get_metodo_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    agendamento_codigo = serializers.CharField(source='agendamento.codigo', read_only=True)

    class Meta:
        model = Pagamento
        fields = [
            'id',
            'valor',
            'metodo',
            'metodo_display',
            'status',
            'status_display',
            'data_vencimento',
            'realizado_em',
            'codigo_transacao',
            'comprovante',
            'agendamento',
            'agendamento_codigo',
        ]

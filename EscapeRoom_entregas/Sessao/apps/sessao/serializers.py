from rest_framework import serializers

from .models import Sessao


class SessaoSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    resultado_display = serializers.CharField(source='get_resultado_display', read_only=True)
    agendamento_codigo = serializers.CharField(source='agendamento.codigo', read_only=True)
    funcionario_nome = serializers.CharField(source='funcionario.nome', read_only=True)

    class Meta:
        model = Sessao
        fields = [
            'id',
            'codigo',
            'inicio_real',
            'fim_real',
            'status',
            'status_display',
            'resultado',
            'resultado_display',
            'observacoes',
            'pontuacao_final',
            'agendamento',
            'agendamento_codigo',
            'funcionario',
            'funcionario_nome',
        ]

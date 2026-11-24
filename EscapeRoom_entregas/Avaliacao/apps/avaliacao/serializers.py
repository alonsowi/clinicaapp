from rest_framework import serializers

from .models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    sessao_codigo = serializers.CharField(source='sessao.codigo', read_only=True)

    class Meta:
        model = Avaliacao
        fields = [
            'id',
            'nota',
            'comentario',
            'recomendaria',
            'criada_em',
            'resposta_empresa',
            'nota_atendimento',
            'cliente',
            'cliente_nome',
            'sessao',
            'sessao_codigo',
        ]

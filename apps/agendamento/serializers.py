from rest_framework import serializers

from .models import Agendamento


class AgendamentoSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source='id_paciente.nome', read_only=True)
    recepcionista_nome = serializers.CharField(source='id_recep.nome', read_only=True)

    class Meta:
        model = Agendamento
        fields = [
            'id_agendamento',
            'chamado',
            'data',
            'horario',
            'id_paciente',
            'id_recep',
            'paciente_nome',
            'recepcionista_nome',
        ]

from rest_framework import serializers

from .models import Recepcionista


class RecepcionistaSerializer(serializers.ModelSerializer):
    turno_display = serializers.CharField(source='get_turno_display', read_only=True)

    class Meta:
        model = Recepcionista
        fields = ['id_recep', 'nome', 'telefone', 'cpf', 'turno', 'turno_display']

from django.db import models

from paciente.models import Paciente
from recepcionista.models import Recepcionista


class Agendamento(models.Model):
    """Horario de consulta de um paciente na clinica (Classe 10)."""

    id_agendamento = models.AutoField(primary_key=True, verbose_name='Codigo')
    chamado = models.IntegerField('Numero do chamado')
    horario = models.TimeField('Horario da consulta')
    data = models.DateField('Data da consulta')
    id_paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        db_column='id_paciente',
        related_name='agendamentos',
        verbose_name='Paciente',
    )
    id_recep = models.ForeignKey(
        Recepcionista,
        on_delete=models.CASCADE,
        db_column='id_recep',
        related_name='agendamentos',
        verbose_name='Recepcionista',
    )

    class Meta:
        db_table = 'agendamento'
        ordering = ['data', 'horario']
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self):
        return f'Chamado {self.chamado} - {self.data:%d/%m/%Y} as {self.horario:%H:%M}'

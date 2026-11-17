from django.db import models


class Recepcionista(models.Model):
    """Funcionario que trabalha na recepcao da clinica (Classe 9)."""

    MANHA = 'Manha'
    TARDE = 'Tarde'
    NOITE = 'Noite'

    TURNO_CHOICES = [
        (MANHA, 'Manha'),
        (TARDE, 'Tarde'),
        (NOITE, 'Noite'),
    ]

    id_recep = models.AutoField(primary_key=True, verbose_name='Codigo')
    nome = models.CharField('Nome completo', max_length=150)
    telefone = models.CharField('Telefone', max_length=20)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    turno = models.CharField('Turno', max_length=20, choices=TURNO_CHOICES)

    class Meta:
        db_table = 'recepcionista'
        ordering = ['nome']
        verbose_name = 'Recepcionista'
        verbose_name_plural = 'Recepcionistas'

    def __str__(self):
        return f'{self.nome} ({self.turno})'

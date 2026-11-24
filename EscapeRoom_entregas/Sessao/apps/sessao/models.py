from django.db import models


class Sessao(models.Model):
    """Sessao de jogo realizada no escape room."""

    AGENDADA = 'agendada'
    EM_ANDAMENTO = 'em_andamento'
    CONCLUIDA = 'concluida'
    CANCELADA = 'cancelada'

    STATUS_CHOICES = [
        (AGENDADA, 'Agendada'),
        (EM_ANDAMENTO, 'Em andamento'),
        (CONCLUIDA, 'Concluida'),
        (CANCELADA, 'Cancelada'),
    ]

    SUCESSO = 'sucesso'
    FALHA = 'falha'
    EMPATE = 'empate'

    RESULTADO_CHOICES = [
        (SUCESSO, 'Sucesso'),
        (FALHA, 'Falha'),
        (EMPATE, 'Empate'),
    ]

    codigo = models.CharField('Codigo', max_length=50, unique=True)
    inicio_real = models.DateTimeField('Inicio real', null=True, blank=True)
    fim_real = models.DateTimeField('Fim real', null=True, blank=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default=AGENDADA)
    resultado = models.CharField('Resultado', max_length=20, choices=RESULTADO_CHOICES, blank=True)
    observacoes = models.TextField('Observacoes', blank=True)
    pontuacao_final = models.IntegerField('Pontuacao final', null=True, blank=True)

    agendamento = models.OneToOneField(
        'agendamento.Agendamento',
        on_delete=models.CASCADE,
        related_name='sessao',
        verbose_name='Agendamento',
    )
    funcionario = models.ForeignKey(
        'funcionario.Funcionario',
        on_delete=models.CASCADE,
        related_name='sessoes',
        verbose_name='Funcionario',
    )

    class Meta:
        db_table = 'sessao'
        ordering = ['-inicio_real', 'codigo']
        verbose_name = 'Sessao'
        verbose_name_plural = 'Sessoes'

    def __str__(self):
        return f'Sessao {self.codigo}'

from django.db import models


class Pagamento(models.Model):
    """Pagamento referente a um agendamento no escape room."""

    PIX = 'pix'
    CARTAO = 'cartao'
    DINHEIRO = 'dinheiro'
    BOLETO = 'boleto'
    TRANSFERENCIA = 'transferencia'

    METODO_CHOICES = [
        (PIX, 'Pix'),
        (CARTAO, 'Cartao'),
        (DINHEIRO, 'Dinheiro'),
        (BOLETO, 'Boleto'),
        (TRANSFERENCIA, 'Transferencia'),
    ]

    PENDENTE = 'pendente'
    PAGO = 'pago'
    CANCELADO = 'cancelado'
    ESTORNADO = 'estornado'

    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (PAGO, 'Pago'),
        (CANCELADO, 'Cancelado'),
        (ESTORNADO, 'Estornado'),
    ]

    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    metodo = models.CharField('Metodo', max_length=20, choices=METODO_CHOICES)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default=PENDENTE)
    data_vencimento = models.DateField('Data de vencimento', null=True, blank=True)
    realizado_em = models.DateTimeField('Realizado em', null=True, blank=True)
    codigo_transacao = models.CharField('Codigo da transacao', max_length=100, unique=True)
    comprovante = models.FileField('Comprovante', upload_to='comprovantes/', blank=True)

    agendamento = models.ForeignKey(
        'agendamento.Agendamento',
        on_delete=models.CASCADE,
        related_name='pagamentos',
        verbose_name='Agendamento',
    )

    class Meta:
        db_table = 'pagamento'
        ordering = ['-realizado_em', 'codigo_transacao']
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return f'Pagamento {self.codigo_transacao}'

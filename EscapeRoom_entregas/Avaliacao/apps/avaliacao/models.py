from django.db import models


class Avaliacao(models.Model):
    """Avaliacao feita pelo cliente apos uma sessao no escape room."""

    nota = models.IntegerField('Nota')
    comentario = models.TextField('Comentario', blank=True)
    recomendaria = models.BooleanField('Recomendaria', default=False)
    criada_em = models.DateTimeField('Criada em', auto_now_add=True)
    resposta_empresa = models.TextField('Resposta da empresa', blank=True)
    nota_atendimento = models.IntegerField('Nota do atendimento', null=True, blank=True)

    cliente = models.ForeignKey(
        'cliente.Cliente',
        on_delete=models.CASCADE,
        related_name='avaliacoes',
        verbose_name='Cliente',
    )
    sessao = models.ForeignKey(
        'sessao.Sessao',
        on_delete=models.CASCADE,
        related_name='avaliacoes',
        verbose_name='Sessao',
    )

    class Meta:
        db_table = 'avaliacao'
        ordering = ['-criada_em']
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'

    def __str__(self):
        return f'Avaliacao #{self.pk} - nota {self.nota}'

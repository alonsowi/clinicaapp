from django.db import models


class Paciente(models.Model):
    """Paciente da clinica.

    Modelo de apoio: o Agendamento aponta para um paciente atraves de
    ForeignKey, por isso ele e criado junto com o projeto.
    """

    id_paciente = models.AutoField(primary_key=True, verbose_name='Codigo')
    nome = models.CharField('Nome completo', max_length=150)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    data_nascimento = models.DateField('Data de nascimento', blank=True, null=True)

    class Meta:
        db_table = 'paciente'
        ordering = ['nome']
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.nome

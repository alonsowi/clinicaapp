# Migration escrita manualmente: os apps "agendamento" e "funcionario"
# (de outros colegas) ainda nao existem neste projeto, entao o comando
# makemigrations nao consegue gerar este arquivo. Apos integrar os apps,
# rode "python manage.py makemigrations --check --dry-run" para conferir.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Codigo')),
                ('inicio_real', models.DateTimeField(blank=True, null=True, verbose_name='Inicio real')),
                ('fim_real', models.DateTimeField(blank=True, null=True, verbose_name='Fim real')),
                ('status', models.CharField(choices=[('agendada', 'Agendada'), ('em_andamento', 'Em andamento'), ('concluida', 'Concluida'), ('cancelada', 'Cancelada')], default='agendada', max_length=20, verbose_name='Status')),
                ('resultado', models.CharField(blank=True, choices=[('sucesso', 'Sucesso'), ('falha', 'Falha'), ('empate', 'Empate')], max_length=20, verbose_name='Resultado')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observacoes')),
                ('pontuacao_final', models.IntegerField(blank=True, null=True, verbose_name='Pontuacao final')),
                ('agendamento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sessao', to='agendamento.agendamento', verbose_name='Agendamento')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessoes', to='funcionario.funcionario', verbose_name='Funcionario')),
            ],
            options={
                'verbose_name': 'Sessao',
                'verbose_name_plural': 'Sessoes',
                'db_table': 'sessao',
                'ordering': ['-inicio_real', 'codigo'],
            },
        ),
    ]

# Migration escrita manualmente: o app "cliente" (de outro colega) ainda nao
# existe neste projeto, entao o comando makemigrations nao consegue gerar este
# arquivo. Apos integrar o app, rode "makemigrations --check --dry-run".

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(verbose_name='Nota')),
                ('comentario', models.TextField(blank=True, verbose_name='Comentario')),
                ('recomendaria', models.BooleanField(default=False, verbose_name='Recomendaria')),
                ('criada_em', models.DateTimeField(auto_now_add=True, verbose_name='Criada em')),
                ('resposta_empresa', models.TextField(blank=True, verbose_name='Resposta da empresa')),
                ('nota_atendimento', models.IntegerField(blank=True, null=True, verbose_name='Nota do atendimento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='cliente.cliente', verbose_name='Cliente')),
                ('sessao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='sessao.sessao', verbose_name='Sessao')),
            ],
            options={
                'verbose_name': 'Avaliacao',
                'verbose_name_plural': 'Avaliacoes',
                'db_table': 'avaliacao',
                'ordering': ['-criada_em'],
            },
        ),
    ]

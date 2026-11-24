# Migration escrita manualmente: o app "agendamento" (de outro colega) ainda
# nao existe neste projeto, entao o comando makemigrations nao consegue gerar
# este arquivo. Apos integrar o app, rode "makemigrations --check --dry-run".

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('metodo', models.CharField(choices=[('pix', 'Pix'), ('cartao', 'Cartao'), ('dinheiro', 'Dinheiro'), ('boleto', 'Boleto'), ('transferencia', 'Transferencia')], max_length=20, verbose_name='Metodo')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('pago', 'Pago'), ('cancelado', 'Cancelado'), ('estornado', 'Estornado')], default='pendente', max_length=20, verbose_name='Status')),
                ('data_vencimento', models.DateField(blank=True, null=True, verbose_name='Data de vencimento')),
                ('realizado_em', models.DateTimeField(blank=True, null=True, verbose_name='Realizado em')),
                ('codigo_transacao', models.CharField(max_length=100, unique=True, verbose_name='Codigo da transacao')),
                ('comprovante', models.FileField(blank=True, upload_to='comprovantes/', verbose_name='Comprovante')),
                ('agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamentos', to='agendamento.agendamento', verbose_name='Agendamento')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'db_table': 'pagamento',
                'ordering': ['-realizado_em', 'codigo_transacao'],
            },
        ),
    ]

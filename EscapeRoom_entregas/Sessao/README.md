# Sessao - parte individual (Django + DRF)

Pasta independente com a implementacao da classe **Sessao** do diagrama
EscapeRoom. Esta e uma copia do app do projeto `EscapeRoom` (o original
continua intacto).

## Conteudo

```
Sessao/
  apps/sessao/                  # app Django
    models.py                   # model Sessao
    views.py                    # 4 views MVT + SessaoViewSet (API)
    urls.py                     # rotas HTML + roteador DRF (/api/)
    serializers.py              # SessaoSerializer
    admin.py
    migrations/0001_initial.py  # migration escrita a mao
  templates/sessao/             # 3 paginas HTML (list, form, confirm delete)
  INTEGRACAO.md                 # como ligar este app em um projeto Django
```

## Campos do model

`codigo`, `inicio_real`, `fim_real`, `status`, `resultado`, `observacoes`,
`pontuacao_final`, `agendamento` (OneToOne), `funcionario` (FK).

## Endpoints apos integrar

| Tipo | URL |
| --- | --- |
| HTML - listar | `/sessoes/` |
| HTML - cadastrar | `/sessoes/novo/` |
| API REST | `/sessoes/api/` |

## Dependencias

Referencia `agendamento.Agendamento` e `funcionario.Funcionario`, que devem
vir dos apps dos colegas. Ate eles existirem, `manage.py check` e
`makemigrations` nao validam. A migration ja esta inclusa.

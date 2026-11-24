# Pagamento - parte individual (Django + DRF)

Pasta independente com a implementacao da classe **Pagamento** do diagrama
EscapeRoom. Esta e uma copia do app do projeto `EscapeRoom` (o original
continua intacto).

## Conteudo

```
Pagamento/
  apps/pagamento/                 # app Django
    models.py                     # model Pagamento
    views.py                      # 4 views MVT + PagamentoViewSet (API)
    urls.py                       # rotas HTML + roteador DRF (/api/)
    serializers.py                # PagamentoSerializer
    admin.py
    migrations/0001_initial.py    # migration escrita a mao
  templates/pagamento/            # 3 paginas HTML (list, form, confirm delete)
  INTEGRACAO.md                   # como ligar este app em um projeto Django
```

## Campos do model

`valor`, `metodo`, `status`, `data_vencimento`, `realizado_em`,
`codigo_transacao`, `comprovante`, `agendamento` (FK).

## Endpoints apos integrar

| Tipo | URL |
| --- | --- |
| HTML - listar | `/pagamentos/` |
| HTML - cadastrar | `/pagamentos/novo/` |
| API REST | `/pagamentos/api/` |

## Dependencias

Referencia `agendamento.Agendamento`, que deve vir do app de outro colega.
Ate ele existir, `manage.py check` e `makemigrations` nao validam. A migration
ja esta inclusa.

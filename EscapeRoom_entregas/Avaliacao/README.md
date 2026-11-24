# Avaliacao - parte individual (Django + DRF)

Pasta independente com a implementacao da classe **Avaliacao** do diagrama
EscapeRoom. Esta e uma copia do app do projeto `EscapeRoom` (o original
continua intacto).

## Conteudo

```
Avaliacao/
  apps/avaliacao/                 # app Django
    models.py                     # model Avaliacao
    views.py                      # 4 views MVT + AvaliacaoViewSet (API)
    urls.py                       # rotas HTML + roteador DRF (/api/)
    serializers.py                # AvaliacaoSerializer
    admin.py
    migrations/0001_initial.py    # migration escrita a mao
  templates/avaliacao/            # 3 paginas HTML (list, form, confirm delete)
  INTEGRACAO.md                   # como ligar este app em um projeto Django
```

## Campos do model

`nota`, `comentario`, `recomendaria`, `criada_em`, `resposta_empresa`,
`nota_atendimento`, `cliente` (FK), `sessao` (FK).

## Endpoints apos integrar

| Tipo | URL |
| --- | --- |
| HTML - listar | `/avaliacoes/` |
| HTML - cadastrar | `/avaliacoes/novo/` |
| API REST | `/avaliacoes/api/` |

## Dependencias

Referencia `cliente.Cliente` (app de outro colega) e `sessao.Sessao`. A
migration `0001_initial.py` depende de `sessao.0001_initial` — se for enviar
esta parte isoladamente, inclua tambem a migration do app Sessao.

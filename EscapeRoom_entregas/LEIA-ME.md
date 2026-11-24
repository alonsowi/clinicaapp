# Entregas separadas - EscapeRoom

Este diretorio contem **3 pastas independentes**, uma para cada classe do
diagrama. O projeto completo original (`C:\Users\alons\OneDrive\Documentos\EscapeRoom`)
nao foi alterado.

```
EscapeRoom_entregas/
  Sessao/       -> app sessao + templates + README + INTEGRACAO
  Avaliacao/    -> app avaliacao + templates + README + INTEGRACAO
  Pagamento/    -> app pagamento + templates + README + INTEGRACAO
  Sessao.zip
  Avaliacao.zip
  Pagamento.zip
```

Cada pasta pode ser enviada separadamente. Dentro dela:

- `apps/<app>/` - codigo Django (model, views MVT, viewset DRF, serializer,
  URLs, admin, migration);
- `templates/<app>/` - os 3 HTML da parte MVT;
- `README.md` - resumo da classe e endpoints;
- `INTEGRACAO.md` - trechos exatos para adicionar em `settings.py`, `urls.py`
  e templates do projeto.

## Observacao

As classes dependem de `agendamento.Agendamento`, `funcionario.Funcionario` e
`cliente.Cliente` (apps de outros colegas, nao criados aqui). Por isso um
destes diretorios sozinho nao e um projeto executavel: ele e a **parte
individual** a ser integrada. As migrations estao inclusas em cada app.

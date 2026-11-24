# Como integrar o app Pagamento

1. Copie a pasta `apps/pagamento` para `apps/pagamento` do projeto.
2. Copie a pasta `templates/pagamento` para `templates/pagamento` do projeto.
3. No `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'pagamento.apps.PagamentoConfig',
]
```

Se o projeto usar `apps/` como pacote, garanta o `sys.path`:

```python
import os, sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```

4. No `urls.py` do projeto:

```python
from django.urls import include, path

urlpatterns = [
    # ...
    path('pagamentos/', include('pagamento.urls', namespace='pagamento')),
]
```

5. Nos templates, os links opcionais do menu (`templates/base.html`) e do
   dashboard (`templates/core/home.html`):

```html
<a href="{% url 'pagamento:list' %}">Pagamentos</a>
```

6. Apos o colega adicionar o app `agendamento`:

```bash
python manage.py makemigrations --check --dry-run
python manage.py migrate
```

## Commits no repositorio original (branch `pagamento`)

1. `feat(pagamento): cria o model Pagamento`
2. `feat(pagamento): cria as views MVT (listar, cadastrar, editar, excluir)`
3. `feat(pagamento): define as URLs e adiciona o app ao menu`
4. `feat(pagamento): cria os templates HTML (UDWMJ)`
5. `feat(pagamento): cria o serializer (SDM)`
6. `feat(pagamento): expoe a API REST (viewset e rotas)`
7. `chore(pagamento): adiciona migration inicial`

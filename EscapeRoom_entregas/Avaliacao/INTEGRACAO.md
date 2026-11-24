# Como integrar o app Avaliacao

1. Copie a pasta `apps/avaliacao` para `apps/avaliacao` do projeto.
2. Copie a pasta `templates/avaliacao` para `templates/avaliacao` do projeto.
3. No `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'sessao.apps.SessaoConfig',
    'avaliacao.apps.AvaliacaoConfig',
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
    path('avaliacoes/', include('avaliacao.urls', namespace='avaliacao')),
]
```

5. Nos templates, os links opcionais do menu (`templates/base.html`) e do
   dashboard (`templates/core/home.html`):

```html
<a href="{% url 'avaliacao:list' %}">Avaliacoes</a>
```

6. A migration depende de `sessao.0001_initial` e do app `cliente` (de outro
   colega). Apos integrar ambos:

```bash
python manage.py makemigrations --check --dry-run
python manage.py migrate
```

## Commits no repositorio original (branch `avaliacao`)

1. `feat(avaliacao): cria o model Avaliacao`
2. `feat(avaliacao): cria as views MVT (listar, cadastrar, editar, excluir)`
3. `feat(avaliacao): define as URLs e adiciona o app ao menu`
4. `feat(avaliacao): cria os templates HTML (UDWMJ)`
5. `feat(avaliacao): cria o serializer (SDM)`
6. `feat(avaliacao): expoe a API REST (viewset e rotas)`
7. `chore(avaliacao): adiciona migration inicial`

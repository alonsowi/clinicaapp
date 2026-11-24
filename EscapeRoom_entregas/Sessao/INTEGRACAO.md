# Como integrar o app Sessao

1. Copie a pasta `apps/sessao` para `apps/sessao` do projeto.
2. Copie a pasta `templates/sessao` para `templates/sessao` do projeto.
3. No `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'sessao.apps.SessaoConfig',
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
    path('sessoes/', include('sessao.urls', namespace='sessao')),
]
```

5. Nos templates, os links opcionais do menu (`templates/base.html`) e do
   dashboard (`templates/core/home.html`):

```html
<a href="{% url 'sessao:list' %}">Sessoes</a>
```

6. Apos os colegas adicionarem `agendamento` e `funcionario`:

```bash
python manage.py makemigrations --check --dry-run
python manage.py migrate
```

## Commits no repositorio original (branch `sessao`)

1. `feat(sessao): cria o model Sessao`
2. `feat(sessao): cria as views MVT (listar, cadastrar, editar, excluir)`
3. `feat(sessao): define as URLs e adiciona o app ao menu`
4. `feat(sessao): cria os templates HTML (UDWMJ)`
5. `feat(sessao): cria o serializer (SDM)`
6. `feat(sessao): expoe a API REST (viewset e rotas)`
7. `chore(sessao): adiciona migration inicial`

# 2026-2-UDWMJ-SDM-Quinta-Manha-FAPA-04-MVT-REST

Sistema de gerenciamento de uma clinica medica desenvolvido em **Python/Django**
com **banco de dados Oracle**, contendo a parte **UDWMJ** (Django + HTML, padrao
MVT) e a parte **SDM** (Django REST Framework).

## Classes implementadas

| Classe | App | Campos |
| --- | --- | --- |
| 9 - Recepcionista | `apps/recepcionista` | `id_recep`, `nome`, `telefone`, `cpf`, `turno` |
| 10 - Agendamento | `apps/agendamento` | `id_agendamento`, `chamado`, `horario`, `data`, `id_paciente`, `id_recep` |

O app `apps/paciente` contem um modelo **Paciente** de apoio, necessario para a
chave estrangeira `id_paciente` do Agendamento.

## Estrutura

```
clinicapp/            # configuracoes do projeto (settings, urls)
apps/
  core/               # app base (pagina inicial)
  paciente/           # modelo de apoio Paciente
  recepcionista/      # Classe 9  (models, views, urls, serializers, admin)
  agendamento/        # Classe 10 (models, views, urls, serializers, admin)
templates/            # paginas HTML (MVT)
staticfiles/          # CSS e JavaScript
Wallet_clinicapp/     # wallet do Oracle Autonomous Database
```

## Como executar

1. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   # source .venv/bin/activate # Linux/macOS
   ```

2. Instale as dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure o arquivo `.env` (copie o modelo abaixo e ajuste os dados):

   ```env
   SECRET_KEY=troque-esta-chave
   DEBUG=True
   DB_USER=ADMIN
   DB_PASSWORD=sua-senha
   TNS_NAME=clinicapp_high
   TNS_ADMIN=C:\Clinicapp\Wallet_clinicapp
   WALLET_PASSWORD=sua-senha-do-wallet
   ```

   > A wallet do Oracle deve estar na pasta indicada em `TNS_ADMIN`
   > (a copia enviada no projeto fica em `Wallet_clinicapp/`).

4. Gere e aplique as migracoes:

   ```bash
   python manage.py makemigrations paciente recepcionista agendamento
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

## Endpoints

### UDWMJ (HTML)

| Tela | URL |
| --- | --- |
| Inicio | `/` |
| Pacientes | `/pacientes/` |
| Recepcionistas | `/recepcionistas/` |
| Agendamentos | `/agendamentos/` |
| Administracao | `/admin/` |

### SDM (REST)

| Recurso | URL |
| --- | --- |
| Pacientes | `/pacientes/api/` |
| Recepcionistas | `/recepcionistas/api/` |
| Agendamentos | `/agendamentos/api/` |

## Fluxo Git (branch por classe)

O projeto usa uma branch por classe, conforme solicitado:

- `main` - projeto base + app `paciente`;
- `recepcionista` - Classe 9;
- `agendamento` - Classe 10.

Cada branch possui commits separados para **Model**, **View**, **URL**,
**Template** e **Serializer**.

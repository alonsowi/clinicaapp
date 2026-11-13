from django.apps import AppConfig


class PacienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paciente'
    label = 'paciente_clinica'
    verbose_name = 'Pacientes'

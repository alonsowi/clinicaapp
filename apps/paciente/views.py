from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rest_framework import viewsets

from .models import Paciente
from .serializers import PacienteSerializer


# ---------------------------------------------------------------------------
# UDWMJ - Django com HTML (MVT)
# ---------------------------------------------------------------------------
class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente/paciente_list.html'
    context_object_name = 'pacientes'
    paginate_by = 10


class PacienteCreateView(CreateView):
    model = Paciente
    fields = ['nome', 'cpf', 'telefone', 'data_nascimento']
    template_name = 'paciente/paciente_form.html'
    success_url = reverse_lazy('paciente:list')


# ---------------------------------------------------------------------------
# SDM - Django REST Framework
# ---------------------------------------------------------------------------
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

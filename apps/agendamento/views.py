from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework import viewsets

from .models import Agendamento
from .serializers import AgendamentoSerializer


# ---------------------------------------------------------------------------
# UDWMJ - Django com HTML (MVT)
# ---------------------------------------------------------------------------
class AgendamentoListView(ListView):
    """Consulta de agendamentos."""

    model = Agendamento
    template_name = 'agendamento/agendamento_list.html'
    context_object_name = 'agendamentos'
    paginate_by = 10

    def get_queryset(self):
        return Agendamento.objects.select_related('id_paciente', 'id_recep')


class AgendamentoCreateView(CreateView):
    """Cadastro de um novo agendamento."""

    model = Agendamento
    fields = ['chamado', 'data', 'horario', 'id_paciente', 'id_recep']
    template_name = 'agendamento/agendamento_form.html'
    success_url = reverse_lazy('agendamento:list')

    def form_valid(self, form):
        messages.success(self.request, 'Agendamento cadastrado com sucesso!')
        return super().form_valid(form)


class AgendamentoUpdateView(UpdateView):
    """Edicao de um agendamento existente."""

    model = Agendamento
    fields = ['chamado', 'data', 'horario', 'id_paciente', 'id_recep']
    template_name = 'agendamento/agendamento_form.html'
    success_url = reverse_lazy('agendamento:list')

    def form_valid(self, form):
        messages.success(self.request, 'Agendamento atualizado com sucesso!')
        return super().form_valid(form)


class AgendamentoDeleteView(DeleteView):
    """Exclusao de um agendamento."""

    model = Agendamento
    template_name = 'agendamento/agendamento_confirm_delete.html'
    success_url = reverse_lazy('agendamento:list')

    def form_valid(self, form):
        messages.success(self.request, 'Agendamento excluido com sucesso!')
        return super().form_valid(form)


# ---------------------------------------------------------------------------
# SDM - Django REST Framework
# ---------------------------------------------------------------------------
class AgendamentoViewSet(viewsets.ModelViewSet):
    """CRUD completo da API REST de agendamentos."""

    queryset = Agendamento.objects.select_related('id_paciente', 'id_recep')
    serializer_class = AgendamentoSerializer

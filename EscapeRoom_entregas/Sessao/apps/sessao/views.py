from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework import viewsets

from .models import Sessao
from .serializers import SessaoSerializer


# ---------------------------------------------------------------------------
# UDWMJ - Django com HTML (MVT)
# ---------------------------------------------------------------------------
class SessaoListView(ListView):
    """Consulta de sessoes."""

    model = Sessao
    template_name = 'sessao/sessao_list.html'
    context_object_name = 'sessoes'
    paginate_by = 10

    def get_queryset(self):
        return Sessao.objects.select_related('agendamento', 'funcionario')


class SessaoCreateView(CreateView):
    """Cadastro de uma nova sessao."""

    model = Sessao
    fields = [
        'codigo', 'inicio_real', 'fim_real', 'status', 'resultado',
        'observacoes', 'pontuacao_final', 'agendamento', 'funcionario',
    ]
    template_name = 'sessao/sessao_form.html'
    success_url = reverse_lazy('sessao:list')

    def form_valid(self, form):
        messages.success(self.request, 'Sessao cadastrada com sucesso!')
        return super().form_valid(form)


class SessaoUpdateView(UpdateView):
    """Edicao de uma sessao existente."""

    model = Sessao
    fields = [
        'codigo', 'inicio_real', 'fim_real', 'status', 'resultado',
        'observacoes', 'pontuacao_final', 'agendamento', 'funcionario',
    ]
    template_name = 'sessao/sessao_form.html'
    success_url = reverse_lazy('sessao:list')

    def form_valid(self, form):
        messages.success(self.request, 'Sessao atualizada com sucesso!')
        return super().form_valid(form)


class SessaoDeleteView(DeleteView):
    """Exclusao de uma sessao."""

    model = Sessao
    template_name = 'sessao/sessao_confirm_delete.html'
    success_url = reverse_lazy('sessao:list')

    def form_valid(self, form):
        messages.success(self.request, 'Sessao excluida com sucesso!')
        return super().form_valid(form)


# ---------------------------------------------------------------------------
# SDM - Django REST Framework
# ---------------------------------------------------------------------------
class SessaoViewSet(viewsets.ModelViewSet):
    """CRUD completo da API REST de sessoes."""

    queryset = Sessao.objects.select_related('agendamento', 'funcionario')
    serializer_class = SessaoSerializer

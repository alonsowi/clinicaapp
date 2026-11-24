from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework import viewsets

from .models import Pagamento
from .serializers import PagamentoSerializer


# ---------------------------------------------------------------------------
# UDWMJ - Django com HTML (MVT)
# ---------------------------------------------------------------------------
class PagamentoListView(ListView):
    """Consulta de pagamentos."""

    model = Pagamento
    template_name = 'pagamento/pagamento_list.html'
    context_object_name = 'pagamentos'
    paginate_by = 10

    def get_queryset(self):
        return Pagamento.objects.select_related('agendamento')


class PagamentoCreateView(CreateView):
    """Cadastro de um novo pagamento."""

    model = Pagamento
    fields = [
        'valor', 'metodo', 'status', 'data_vencimento', 'realizado_em',
        'codigo_transacao', 'comprovante', 'agendamento',
    ]
    template_name = 'pagamento/pagamento_form.html'
    success_url = reverse_lazy('pagamento:list')

    def form_valid(self, form):
        messages.success(self.request, 'Pagamento cadastrado com sucesso!')
        return super().form_valid(form)


class PagamentoUpdateView(UpdateView):
    """Edicao de um pagamento existente."""

    model = Pagamento
    fields = [
        'valor', 'metodo', 'status', 'data_vencimento', 'realizado_em',
        'codigo_transacao', 'comprovante', 'agendamento',
    ]
    template_name = 'pagamento/pagamento_form.html'
    success_url = reverse_lazy('pagamento:list')

    def form_valid(self, form):
        messages.success(self.request, 'Pagamento atualizado com sucesso!')
        return super().form_valid(form)


class PagamentoDeleteView(DeleteView):
    """Exclusao de um pagamento."""

    model = Pagamento
    template_name = 'pagamento/pagamento_confirm_delete.html'
    success_url = reverse_lazy('pagamento:list')

    def form_valid(self, form):
        messages.success(self.request, 'Pagamento excluido com sucesso!')
        return super().form_valid(form)


# ---------------------------------------------------------------------------
# SDM - Django REST Framework
# ---------------------------------------------------------------------------
class PagamentoViewSet(viewsets.ModelViewSet):
    """CRUD completo da API REST de pagamentos."""

    queryset = Pagamento.objects.select_related('agendamento')
    serializer_class = PagamentoSerializer

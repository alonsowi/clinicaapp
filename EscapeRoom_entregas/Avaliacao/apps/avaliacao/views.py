from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework import viewsets

from .models import Avaliacao
from .serializers import AvaliacaoSerializer


# ---------------------------------------------------------------------------
# UDWMJ - Django com HTML (MVT)
# ---------------------------------------------------------------------------
class AvaliacaoListView(ListView):
    """Consulta de avaliacoes."""

    model = Avaliacao
    template_name = 'avaliacao/avaliacao_list.html'
    context_object_name = 'avaliacoes'
    paginate_by = 10

    def get_queryset(self):
        return Avaliacao.objects.select_related('cliente', 'sessao')


class AvaliacaoCreateView(CreateView):
    """Cadastro de uma nova avaliacao."""

    model = Avaliacao
    fields = [
        'nota', 'comentario', 'recomendaria', 'resposta_empresa',
        'nota_atendimento', 'cliente', 'sessao',
    ]
    template_name = 'avaliacao/avaliacao_form.html'
    success_url = reverse_lazy('avaliacao:list')

    def form_valid(self, form):
        messages.success(self.request, 'Avaliacao cadastrada com sucesso!')
        return super().form_valid(form)


class AvaliacaoUpdateView(UpdateView):
    """Edicao de uma avaliacao existente."""

    model = Avaliacao
    fields = [
        'nota', 'comentario', 'recomendaria', 'resposta_empresa',
        'nota_atendimento', 'cliente', 'sessao',
    ]
    template_name = 'avaliacao/avaliacao_form.html'
    success_url = reverse_lazy('avaliacao:list')

    def form_valid(self, form):
        messages.success(self.request, 'Avaliacao atualizada com sucesso!')
        return super().form_valid(form)


class AvaliacaoDeleteView(DeleteView):
    """Exclusao de uma avaliacao."""

    model = Avaliacao
    template_name = 'avaliacao/avaliacao_confirm_delete.html'
    success_url = reverse_lazy('avaliacao:list')

    def form_valid(self, form):
        messages.success(self.request, 'Avaliacao excluida com sucesso!')
        return super().form_valid(form)


# ---------------------------------------------------------------------------
# SDM - Django REST Framework
# ---------------------------------------------------------------------------
class AvaliacaoViewSet(viewsets.ModelViewSet):
    """CRUD completo da API REST de avaliacoes."""

    queryset = Avaliacao.objects.select_related('cliente', 'sessao')
    serializer_class = AvaliacaoSerializer

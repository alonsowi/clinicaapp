from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework import viewsets

from .models import Recepcionista
from .serializers import RecepcionistaSerializer


# ---------------------------------------------------------------------------
# UDWMJ - Django com HTML (MVT)
# ---------------------------------------------------------------------------
class RecepcionistaListView(ListView):
    """Consulta de recepcionistas."""

    model = Recepcionista
    template_name = 'recepcionista/recepcionista_list.html'
    context_object_name = 'recepcionistas'
    paginate_by = 10


class RecepcionistaCreateView(CreateView):
    """Cadastro de um novo recepcionista."""

    model = Recepcionista
    fields = ['nome', 'telefone', 'cpf', 'turno']
    template_name = 'recepcionista/recepcionista_form.html'
    success_url = reverse_lazy('recepcionista:list')

    def form_valid(self, form):
        messages.success(self.request, 'Recepcionista cadastrado(a) com sucesso!')
        return super().form_valid(form)


class RecepcionistaUpdateView(UpdateView):
    """Edicao de um recepcionista existente."""

    model = Recepcionista
    fields = ['nome', 'telefone', 'cpf', 'turno']
    template_name = 'recepcionista/recepcionista_form.html'
    success_url = reverse_lazy('recepcionista:list')

    def form_valid(self, form):
        messages.success(self.request, 'Recepcionista atualizado(a) com sucesso!')
        return super().form_valid(form)


class RecepcionistaDeleteView(DeleteView):
    """Exclusao de um recepcionista."""

    model = Recepcionista
    template_name = 'recepcionista/recepcionista_confirm_delete.html'
    success_url = reverse_lazy('recepcionista:list')

    def form_valid(self, form):
        messages.success(self.request, 'Recepcionista excluido(a) com sucesso!')
        return super().form_valid(form)


# ---------------------------------------------------------------------------
# SDM - Django REST Framework
# ---------------------------------------------------------------------------
class RecepcionistaViewSet(viewsets.ModelViewSet):
    """CRUD completo da API REST de recepcionistas."""

    queryset = Recepcionista.objects.all()
    serializer_class = RecepcionistaSerializer

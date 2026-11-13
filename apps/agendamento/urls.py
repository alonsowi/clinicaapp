from django.urls import path

from . import views

app_name = 'agendamento'

urlpatterns = [
    # UDWMJ - Django com HTML (MVT)
    path('', views.AgendamentoListView.as_view(), name='list'),
    path('novo/', views.AgendamentoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.AgendamentoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.AgendamentoDeleteView.as_view(), name='delete'),
]

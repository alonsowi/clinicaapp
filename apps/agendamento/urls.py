from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'agendamento'

router = DefaultRouter()
router.register(r'api', views.AgendamentoViewSet, basename='agendamento')

urlpatterns = [
    # UDWMJ - Django com HTML (MVT)
    path('', views.AgendamentoListView.as_view(), name='list'),
    path('novo/', views.AgendamentoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.AgendamentoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.AgendamentoDeleteView.as_view(), name='delete'),

    # SDM - Django REST Framework
    path('', include(router.urls)),
]

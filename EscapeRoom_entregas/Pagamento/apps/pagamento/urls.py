from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'pagamento'

router = DefaultRouter()
router.register(r'api', views.PagamentoViewSet, basename='pagamento')

urlpatterns = [
    # UDWMJ - Django com HTML (MVT)
    path('', views.PagamentoListView.as_view(), name='list'),
    path('novo/', views.PagamentoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.PagamentoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.PagamentoDeleteView.as_view(), name='delete'),

    # SDM - Django REST Framework
    path('', include(router.urls)),
]

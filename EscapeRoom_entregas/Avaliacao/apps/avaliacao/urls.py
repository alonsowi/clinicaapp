from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'avaliacao'

router = DefaultRouter()
router.register(r'api', views.AvaliacaoViewSet, basename='avaliacao')

urlpatterns = [
    # UDWMJ - Django com HTML (MVT)
    path('', views.AvaliacaoListView.as_view(), name='list'),
    path('novo/', views.AvaliacaoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.AvaliacaoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.AvaliacaoDeleteView.as_view(), name='delete'),

    # SDM - Django REST Framework
    path('', include(router.urls)),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'sessao'

router = DefaultRouter()
router.register(r'api', views.SessaoViewSet, basename='sessao')

urlpatterns = [
    # UDWMJ - Django com HTML (MVT)
    path('', views.SessaoListView.as_view(), name='list'),
    path('novo/', views.SessaoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.SessaoUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.SessaoDeleteView.as_view(), name='delete'),

    # SDM - Django REST Framework
    path('', include(router.urls)),
]

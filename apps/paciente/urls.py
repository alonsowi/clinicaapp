from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'paciente'

router = DefaultRouter()
router.register(r'api', views.PacienteViewSet, basename='paciente')

urlpatterns = [
    # UDWMJ - Django com HTML (MVT)
    path('', views.PacienteListView.as_view(), name='list'),
    path('novo/', views.PacienteCreateView.as_view(), name='create'),

    # SDM - Django REST Framework
    path('', include(router.urls)),
]

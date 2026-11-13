from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'recepcionista'

router = DefaultRouter()
router.register(r'api', views.RecepcionistaViewSet, basename='recepcionista')

urlpatterns = [
    # UDWMJ - Django com HTML (MVT)
    path('', views.RecepcionistaListView.as_view(), name='list'),
    path('novo/', views.RecepcionistaCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.RecepcionistaUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.RecepcionistaDeleteView.as_view(), name='delete'),

    # SDM - Django REST Framework
    path('', include(router.urls)),
]

from django.urls import path

from . import views

app_name = 'recepcionista'

urlpatterns = [
    # UDWMJ - Django com HTML (MVT)
    path('', views.RecepcionistaListView.as_view(), name='list'),
    path('novo/', views.RecepcionistaCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.RecepcionistaUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.RecepcionistaDeleteView.as_view(), name='delete'),
]

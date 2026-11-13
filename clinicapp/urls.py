from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('pacientes/', include('paciente.urls', namespace='paciente')),
    path('recepcionistas/', include('recepcionista.urls', namespace='recepcionista')),
    path('agendamentos/', include('agendamento.urls', namespace='agendamento')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

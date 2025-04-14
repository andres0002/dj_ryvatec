from django.urls import path
from apps.user.views_client import PerfilCliente

urlpatterns = [
    path('perfil-cliente/', PerfilCliente.as_view(), name='perfil_cliente'),
]
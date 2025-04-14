from django.urls import path
from apps.user.views_supplier import (
    PerfilProveedor, ListarDispositivos, AdicionarDispositivo, VisualizarDispositivo,
    ModificarDispositivo, BorrarDispositivo, Home, Proveedores, Tecnicos, QuienesSomos
)

urlpatterns = [
    path('perfil-proveedor/', PerfilProveedor.as_view(), name='perfil_proveedor'),
    path('listar-dispositivos/', ListarDispositivos.as_view(), name='listar_dispositivos'),
    path('adicionar-dispositivos/', AdicionarDispositivo.as_view(), name='adicionar_dispositivos'),
    path('visualizar-dispositivos/<int:id_dispositivo>/', VisualizarDispositivo.as_view(), name='visualizar_dispositivos'),
    path('modificar-dispositivos/<int:id_dispositivo>/', ModificarDispositivo.as_view(), name='modificar_dispositivos'),
    path('borrar-dispositivos/<int:id_dispositivo>/', BorrarDispositivo.as_view(), name='borrar_dispositivos'),
    path('home', Home.as_view(), name='home'),
    path('proveedores/', Proveedores.as_view(), name='proveedores'),
    path('tecnicos/', Tecnicos.as_view(), name='tecnicos'),
    path('quienes-somos/', QuienesSomos.as_view(), name='quienes_somos'),
]
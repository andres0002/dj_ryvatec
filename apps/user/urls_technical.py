# django
from django.urls import path
# third
# own
from apps.user.views_technical import PerfilTecnico, Home, Proveedores, Tecnicos, QuienesSomos

urlpatterns = [
    path('perfil-tecnico/', PerfilTecnico.as_view(), name='perfil_tecnico'),
    path('home', Home.as_view(), name='home'),
    path('proveedores/', Proveedores.as_view(), name='proveedores'),
    path('tecnicos/', Tecnicos.as_view(), name='tecnicos'),
    path('quienes-somos/', QuienesSomos.as_view(), name='quienes_somos'),
]
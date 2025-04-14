from django.urls import path
from apps.user.views_administrator import (
    ListadoUsuarios, PerfilAdministrador, AdicionarUsuario, VisualizarUsuario,
    ModificarUsuario, BorrarUsuario, ListarCategoria, AdicionarCategoria,
    VisualizarCategoria, ModificarCategoria, BorrarCategoria, Home,
    Proveedores, Tecnicos, QuienesSomos
)

urlpatterns = [
    path('listar-usuarios/', ListadoUsuarios.as_view(), name='listar_usuarios'),
    path('perfil-administrador/', PerfilAdministrador.as_view(), name='perfil_administrador'),
    path('adicionar-usuarios/', AdicionarUsuario.as_view(), name='adicionar_usuarios'),
    path('visualizar-usuario/<int:id_usuario>/', VisualizarUsuario.as_view(), name='visualizar_usuario'),
    path('modificar-usuario/<int:id_usuario>/', ModificarUsuario.as_view(), name='modificar_usuario'),
    path('borrar-usuario/<int:id_usuario>/', BorrarUsuario.as_view(), name='borrar_usuario'),

    path('listar-categorias/', ListarCategoria.as_view(), name='listar_categoria'),
    path('adicionar-categoria/', AdicionarCategoria.as_view(), name='adicionar_categoria'),
    path('visualizar-categoria/<int:id_categoria>/', VisualizarCategoria.as_view(), name='visualizar_categoria'),
    path('modificar-categoria/<int:id_categoria>/', ModificarCategoria.as_view(), name='modificar_categoria'),
    path('borrar-categoria/<int:id_categoria>/', BorrarCategoria.as_view(), name='borrar_categoria'),

    path('home/', Home.as_view(), name='home'),
    path('proveedores/', Proveedores.as_view(), name='proveedores'),
    path('tecnicos/', Tecnicos.as_view(), name='tecnicos'),
    path('quienes-somos/', QuienesSomos.as_view(), name='quienes_somos'),
]

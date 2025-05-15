# django
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# third
# own
from apps.user.models import Usuario, Dispositivo, Categoria

# Register your models here.

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario
        import_id_fields = ['id_user']  # <--- Esto es CLAVE para evitar el error 'id' si el id o pk por default no es 'id' se debe especificar.

class UsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('nombre','apellido','telefono','direccion','correo','pagina','especialidad','usuid','rol','created_at','updated_at')
    list_display = ('nombre','apellido','telefono','direccion','correo','pagina','especialidad','usuid','rol','created_at','updated_at')
    list_filter = ('especialidad','rol','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')
    resource_class = UsuarioResource

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
        import_id_fields = ['id_categoria']  # <--- Esto es CLAVE para evitar el error 'id' si el id o pk por default no es 'id' se debe especificar.

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre','created_at','updated_at')
    list_filter = ('created_at','updated_at')
    readonly_fields = ('created_at','updated_at')
    resource_class = CategoriaResource

class DispositivoResource(resources.ModelResource):
    class Meta:
        model = Dispositivo
        import_id_fields = ['id_dispositivo']  # <--- Esto es CLAVE para evitar el error 'id' si el id o pk por default no es 'id' se debe especificar.

class DispositivoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('nombre','descripcion')
    list_display = ('nombre','usuario','categoria','precio','descripcion','created_at','updated_at')
    list_filter = ('created_at','updated_at')
    readonly_fields = ('usuario','categoria','created_at','updated_at')
    resource_class = DispositivoResource

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
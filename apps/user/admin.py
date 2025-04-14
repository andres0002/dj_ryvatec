# django
from django.contrib import admin
# third
# own
from apps.user.models import Usuario, Dispositivo, Categoria

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Dispositivo)
admin.site.register(Categoria)
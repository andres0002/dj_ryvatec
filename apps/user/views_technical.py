# django
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
# third
# own
from apps.user.models import Usuario, Dispositivo
from apps.user.forms import UsuarioForm

# Create your views here.

class PerfilTecnico(LoginRequiredMixin, View):
    '''
        Esta clase se encarga de visualizar y  modificar los datos personales del usuario que se encuentra logeado..
    '''
    login_url = '/'
    template_name = 'technical/perfil_tecnico.html'
    form_class = UsuarioForm

    def get(self, request):
        '''
        Eata funcion nos muestra el formulario de los datos personales del ususario registrado o que se encuentra logeado.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de los datos personales con el formulario correspondiente..
        '''
        try:
            datos_usuario = Usuario.objects.get(usuid=request.user.pk)
            form = self.form_class(instance=datos_usuario)
            return render(request, self.template_name, {'form': form})

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        '''
        Esta funcion modifica los datos personales del ususario que se encuentra logeado, valida si se modifico correctamente o si se presento un erro en la modificacion de los datos.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna a la plantilla de los datos personales o perfil.
        '''
        try:
            datos_usuario = Usuario.objects.get(usuid=request.user.pk)
            form = self.form_class(request.POST, request.FILES, instance=datos_usuario)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Perfil se modificó correctamente')
            else:
                messages.add_message(request, messages.ERROR, 'El Perfil no se pudo modificar')

            return self.get(request)

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class Home(LoginRequiredMixin, View):
    '''
    Esta clase se encarga de mostrarnos la plantilla de inicio.
    '''
    template_name = 'technical/home.html'
    def get(self, request):
        '''
        Esta funcion se encarga de mostrar todos los dispositivos registrados en el sistema de informacion.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de inicio y todos los dispositivos registrados en el sistema.
        '''
        lista_dispositivos = Dispositivo.objects.all()
        return render(request, self.template_name, {'list_dispositivos': lista_dispositivos})

class Proveedores(LoginRequiredMixin, View):
    '''
    Esta clase se encarga de mostrar todos los proveedores registrados en el sistema.
    '''
    template_name = 'technical/proveedores.html'
    def get(self, request):
        '''
        Esta funcion se encarga de mostrar todos los proveedores registrados en el sistema.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de los proveedores y a todos los proveedores registrados en el sistema.
        '''
        lista_proveedores = Usuario.objects.filter(rol='PRO')
        return render(request, self.template_name, {'list_proveedores': lista_proveedores})

class Tecnicos(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar todos los tecnicos registrados en el sistema.'''
    template_name = 'technical/tecnicos.html'
    def get(self, request):
        '''
                Esta funcion se encarga de mostrar todos los tecnicos registrados en el sistema.
                :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                :return: Nos retorna la plantilla de los tecnicos y a todos los tecnicos registrados en el sistema.
                '''
        lista_tecnicos = Usuario.objects.filter(rol='TEC')
        return render(request, self.template_name, {'list_tecnicos': lista_tecnicos})

class QuienesSomos(LoginRequiredMixin, View):
    '''
    Esta clase se encarga de mostrarnos la plantilla de quienes somos.
    '''
    template_name = 'technical/quienes_somos.html'
    def get(self, request):
        '''
        Esta funcion se encarga de mostrar la mision y vision del proyecto ryvatec.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de quienes somos.
        '''
        return render(request, self.template_name)
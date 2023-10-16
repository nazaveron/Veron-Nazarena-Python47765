from django.shortcuts import render
from django.http import HttpResponse
from BlogApp.models import *
from BlogApp.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        miFormulario = Avatarformulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            usario = request.user
            imagen = miFormulario.cleaned_data["imagen"]
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            return render(request, "BlogApp/welcome.html")
    else:
        miFormulario = Avatarformulario()

    return render(request, "BlogApp/agregar_avatar.html", {"miFormulario": miFormulario})


def aboutme(request):
    return render(request, 'BlogApp/aboutme.html')

@login_required
def welcome(request):
    return render(request, 'BlogApp/welcome.html')


def registro(request):

    if request.method == 'POST':

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "BlogApp/welcome.html", {"mensaje": "Usuario creado"})
        
    else:

        form = UsuarioRegistro()
    
    return render(request, "BlogApp/registro.html", {"formulario": form})


def iniciosesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request, user)
                return render(request, "BlogApp/welcome.html", {"mensaje": f"Hola {user}!"})
            else:
                return render(request, "BlogApp/homepage.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(request, "BlogApp/login.html", {"formulario": form})
    else:
        form = AuthenticationForm()
        return render(request, "BlogApp/login.html", {"formulario": form})


@login_required
def editarperfil(request):
    usuario = request.user
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.password = informacion["password"]
            usuario.first_name = informacion["first_name"]


            usuario.save()

            return render(request, 'BlogApp/welcome.html')
        
    else:
            miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, 'BlogApp/editarperfil.html', {"miFormulario":miFormulario, 'usuario': usuario})

#CRUD 1989

class ListaPulsera1989(LoginRequiredMixin, ListView):

    model = pulsera1989

class DetallePulsera1989(LoginRequiredMixin, DetailView):

    model = pulsera1989

class CrearPulsera1989(LoginRequiredMixin, CreateView):

    model = pulsera1989
    success_url = "/TS/1989/list"
    fields = ["autor", "pais", "edad", "color_predominante"]

class ActualizarPulsera1989(LoginRequiredMixin, UpdateView,):

    model = pulsera1989
    success_url = "/TS/1989/list"
    fields = ["autor", "pais", "edad", "color_predominante"]

class BorrarPulsera1989(LoginRequiredMixin, DeleteView):

    model = pulsera1989
    success_url = "/TS/1989/list"

#CRUD Reputation

class ListaReputation(LoginRequiredMixin, ListView):

    model = pulseraReputation

class DetalleReputation(LoginRequiredMixin, DetailView):

    model = pulseraReputation

class CrearReputation(LoginRequiredMixin, CreateView):

    model = pulseraReputation
    success_url = "/TS/reputation/list"
    fields = ["autor", "pais", "edad", "color_predominante"]

class ActualizarReputation(LoginRequiredMixin, UpdateView):

    model = pulseraReputation
    success_url = "/TS/reputation/list"
    fields = ["autor", "pais", "edad", "color_predominante"]

class BorrarReputation(LoginRequiredMixin, DeleteView):

    model = pulseraReputation
    success_url = "/TS/reputation/list"


#CRUD Lover

class ListaLover(LoginRequiredMixin, ListView):

    model = pulseraLover

class DetalleLover(LoginRequiredMixin, DetailView):

    model = pulseraLover

class CrearLover(LoginRequiredMixin, CreateView):

    model = pulseraLover
    success_url = "/TS/lover/list"
    fields = ["autor", "pais", "edad", "color_predominante"]

class ActualizarLover(LoginRequiredMixin, UpdateView):

    model = pulseraLover
    success_url = "/TS/lover/list"
    fields = ["autor", "pais", "edad", "color_predominante"]

class BorrarLover(LoginRequiredMixin, DeleteView):

    model = pulseraLover
    success_url = "/TS/lover/list"


#CRUD Folklore

class ListaFolklore(LoginRequiredMixin, ListView):

    model = pulseraFolklore

class DetalleFolklore(LoginRequiredMixin, DetailView):

    model = pulseraFolklore

class CrearFolklore(LoginRequiredMixin, CreateView):

    model = pulseraFolklore
    success_url = "/TS/folklore/list"
    fields = ["autor", "pais", "edad", "color_predominante"]

class ActualizarFolklore(LoginRequiredMixin, UpdateView):

    model = pulseraFolklore
    success_url = "/TS/folklore/list"
    fields = ["autor", "pais", "edad", "color_predominante"]

class BorrarFolklore(LoginRequiredMixin, DeleteView):

    model = pulseraFolklore
    success_url = "/TS/folklore/list"


@login_required
def buscar_pulsera(request):
    form = Buscar_Form()
    return render(request, "BlogApp/busqueda.html", {"form": form})

@login_required
def resultados(request):
    if request.method == 'GET':
        term = request.GET.get('color_predeterminado', '')
        peliculas_encontradas = pulsera1989.objects.filter(color_predeterminado__icontains=term)

        return render(request, 'BlogApp/resultado_busqueda.html', {"pulseras_encontradas": peliculas_encontradas})
    


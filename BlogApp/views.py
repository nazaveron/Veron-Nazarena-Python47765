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
from django.contrib.auth import update_session_auth_hash

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
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            miFormulario.save()

            nueva_contraseña = request.POST.get('password')
            if nueva_contraseña:
                usuario.set_password(nueva_contraseña)
                usuario.save()
                update_session_auth_hash(request, usuario) 

            return render(request, 'BlogApp/welcome.html')
    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, 'BlogApp/editarperfil.html', {"miFormulario": miFormulario, 'usuario': usuario})

#CRUD 1989

class ListaPulsera1989(LoginRequiredMixin, ListView):

    model = pulsera1989

class DetallePulsera1989(LoginRequiredMixin, DetailView):

    model = pulsera1989

class CrearPulsera1989(LoginRequiredMixin, CreateView):

    model = pulsera1989
    success_url = "/TS/1989/list"
    fields = ["autor", "pais", "edad", "color_predominante", "imagen"]

class ActualizarPulsera1989(LoginRequiredMixin, UpdateView,):

    model = pulsera1989
    success_url = "/TS/1989/list"
    fields = ["autor", "pais", "edad", "color_predominante", "imagen"]

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
    fields = ["autor", "pais", "edad", "color_predominante", "imagen"]

class ActualizarReputation(LoginRequiredMixin, UpdateView):

    model = pulseraReputation
    success_url = "/TS/reputation/list"
    fields = ["autor", "pais", "edad", "color_predominante", "imagen"]

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
    fields = ["autor", "pais", "edad", "color_predominante", "imagen"]

class ActualizarLover(LoginRequiredMixin, UpdateView):

    model = pulseraLover
    success_url = "/TS/lover/list"
    fields = ["autor", "pais", "edad", "color_predominante", "imagen"]

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
    fields = ["autor", "pais", "edad", "color_predominante", "imagen"]

class ActualizarFolklore(LoginRequiredMixin, UpdateView):

    model = pulseraFolklore
    success_url = "/TS/folklore/list"
    fields = ["autor", "pais", "edad", "color_predominante", "imagen"]

class BorrarFolklore(LoginRequiredMixin, DeleteView):

    model = pulseraFolklore
    success_url = "/TS/folklore/list"


@login_required
def buscar_pulsera(request):
    return render(request, "BlogApp/Buscar.html")

@login_required
def resultado_busqueda(request):
    colors = request.GET.getlist("color")

    if colors:
        # Search for the common field in all models
        resultados1 = pulsera1989.objects.filter(color_predominante__in=colors)
        resultados2 = pulseraFolklore.objects.filter(color_predominante__in=colors)
        resultados3 = pulseraLover.objects.filter(color_predominante__in=colors)
        resultados4 = pulseraReputation.objects.filter(color_predominante__in=colors)

        # You can combine the results from different models
        combined_results = list(resultados1) + list(resultados2) + list(resultados3)+ list(resultados4)

        return render(request, "BlogApp/resultado_busqueda.html", {"valor": colors, "res": combined_results})
    else:
        return HttpResponse("No seleccionaste ningún color. Regresá e intentá de nuevo")
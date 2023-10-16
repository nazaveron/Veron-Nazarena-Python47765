from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('aboutme/', aboutme, name="about_me"),
    path('welcome/', welcome, name="welcome"),

    path('login/', iniciosesion, name="login"),
    path('registro/', registro, name="registro"),
    path('logout', LogoutView.as_view(template_name="BlogApp/logout.html"), name="logout"),
    path('editarperfil', editarperfil, name="editarperfil"),


    #CRUD 1989

    path('1989/list', ListaPulsera1989.as_view(), name="ver_1989"),
    path('1989/<int:pk>', DetallePulsera1989.as_view(), name="detalle_1989"),
    path('1989/subir/', CrearPulsera1989.as_view(), name="crear_1989"),
    path('1989/actualizar/<int:pk>',ActualizarPulsera1989.as_view(), name="actualizar_1989"),
    path('1989/eliminar/<int:pk>', BorrarPulsera1989.as_view(), name="borrar_1989"),
    

    #CRUD Reputation

    path('reputation/list', ListaReputation.as_view(), name="ver_reputation"),
    path('reputation/<int:pk>', DetalleReputation.as_view(), name="detalle_reputation"),
    path('reputation/subir/', CrearReputation.as_view(), name="crear_reputation"),
    path('reputation/actualizar/<int:pk>',ActualizarReputation.as_view(), name="actualizar_reputation"),
    path('reputation/eliminar/<int:pk>', BorrarReputation.as_view(), name="borrar_reputation"),

    #CRUD Lover

    path('lover/list', ListaLover.as_view(), name="ver_lover"),
    path('lover/<int:pk>', DetalleLover.as_view(), name="detalle_lover"),
    path('lover/subir/', CrearLover.as_view(), name="crear_lover"),
    path('lover/actualizar/<int:pk>',ActualizarLover.as_view(), name="actualizar_lover"),
    path('lover/eliminar/<int:pk>', BorrarLover.as_view(), name="borrar_lover"),

    
    #CRUD Folklore

    path('folklore/list', ListaFolklore.as_view(), name="ver_folklore"),
    path('folklore/<int:pk>', DetalleFolklore.as_view(), name="detalle_folklore"),
    path('folklore/subir/', CrearFolklore.as_view(), name="crear_folklore"),
    path('folklore/actualizar/<int:pk>',ActualizarFolklore.as_view(), name="actualizar_folklore"),
    path('folklore/eliminar/<int:pk>', BorrarFolklore.as_view(), name="borrar_folklore"),
    ]
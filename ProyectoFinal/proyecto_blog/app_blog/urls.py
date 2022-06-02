from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.inicio_sesion,),
    path("inicio", views.inicio, name="inicio"),
    path("register", views.registarse, name="registrarse"),
    path("registro_usuario", views.registro_usuario),
    path("datos_sesion", views.datos_sesion),
    path("crear_historia", views.crear_historias, name="crearHistoria"),
    path("alta_historias", views.altaHistorias),
    path("historias", views.historias, name="historias"),
    path("formPersonas", views.informacion_personas, name="info_personas"),
    path("alta_personas", views.alta_personas),
    path("personas", views.persona, name="personas"),
    path("buscarPersona", views.buscarPersona)
    
    
    
]
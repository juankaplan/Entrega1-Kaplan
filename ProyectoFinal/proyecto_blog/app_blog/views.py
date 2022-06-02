from re import template
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from app_blog.models import Usuarios, Textos, Personas
from app_blog.forms import form_Usuario, form_texto, form_inicio, form_personas

# Create your views here.

def inicio(request):
    
    return render(request, "inicio.html")


def inicio_sesion(request):
    
    return render(request, "inicio_sesion.html")

def datos_sesion(request):
    if request.method == "POST":
        mi_Formulario = form_inicio(request.POST)
        if mi_Formulario.is_valid():
            informacion_formulario = mi_Formulario.cleaned_data
            usuario = Usuarios.objects.filter(email = informacion_formulario["email"], contraseña = informacion_formulario["contraseña"]).values
            datos = {"usuario": usuario}
            return render(request, "inicio.html", datos)
       
       
            
               
def registarse(request):
    
    return render(request, "register.html")



def crear_historias(request):
    return render(request, "crear_historias.html")




def altaHistorias(request):
    if request.method == "POST":
        mi_Formulario = form_texto(request.POST)
        print(mi_Formulario)
        if mi_Formulario.is_valid():
            informacion_formulario = mi_Formulario.cleaned_data
            texto = Textos(nombre = informacion_formulario["nombre"], texto = informacion_formulario["texto"])
            texto.save()
            return render(request, "crear_historias.html")
        
def historias(request):
    historias = Textos.objects.all()
    datos = {"historias": historias}
    return render(request, "historias.html", datos)

def registro_usuario(request):
    if request.method == "POST":
        mi_Formulario = form_Usuario(request.POST)
        
        print(mi_Formulario)
        
        if mi_Formulario.is_valid:
           informacion_formulario = mi_Formulario.cleaned_data
           usuario = Usuarios(nombre = informacion_formulario["nombre"], email =  informacion_formulario["email"], contraseña = informacion_formulario["contraseña"])
           usuario.save()
           usuario_v2 = Usuarios.objects.filter(email = informacion_formulario["email"], contraseña = informacion_formulario["contraseña"]).values
           datos = {"usuario": usuario_v2}
           return render(request, "inicio.html", datos)
       
       
def informacion_personas(request):
    return render(request, "IngresarPersonas.html")

def alta_personas(request):
    if request.method == "GET":
        mi_formulario = form_personas(request.GET)
        print(mi_formulario)
        if mi_formulario.is_valid():
            informacion_formulario = mi_formulario.cleaned_data
            persona = Personas(nombre = informacion_formulario["nombre"], apellido = informacion_formulario["apellido"],  nacionalidad = informacion_formulario["nacionalidad"], edad = informacion_formulario["edad"])
            persona.save()
            return render(request, "IngresarPersonas.html")
    

def persona(request):
    return render(request, "personas.html")

def buscarPersona(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        persona = Personas.objects.filter(nombre = nombre, apellido = apellido )
        datos = {"persona": persona}
        return render(request, "personas.html", datos)
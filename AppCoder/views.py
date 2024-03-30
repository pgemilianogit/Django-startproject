from django.shortcuts import render
#Importando el modelo dar de alta uno nuevo importando la clase curso
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader


# Create your views here.
#4 Definir las views

#Responder en la platilla renderizada
def inicio(request):
    return render(request, "padre.html")

def alta_curso(request, nombre):
    #contructor de la clase, un objeto mas lo que hereda
    curso = Curso(nombre=nombre, camada= 234512)
    curso.save()
    
    #Dar de alta los registros en la base de datos para insertarlos desde la interfaz
    texto=f"Se guardo en la DB el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_cursos(request):
    #Como ver la base de datos, return lista
    cursos = Curso.objects.all()
    dicc ={"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    #Loader simpl todo el problema de como entrar al template, donde ya definimos
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

#PROCESO:

#crear un diccionario con una sola propiedad (cursos) y el valor sera el conjunto de dicc
#teniendo todos los cursos cargar la plantilla  get_template metodo del motor de plantillas apuntando en settings
#render de la plantilla mandando el diccionario, pasa todo dinamismo, retorna todos los cursos

def alumnos(request):
    return render(request, "alumnos.html")

def profesores(request):
    return render(request, "profesores.html")



def curso_formulario(request):

    if request.method == "POST":
        curso = Curso( nombre=request.POST["nombre"] , camada=request.POST["camada"])
        curso.save()
        return render(request , "formulario.html")

    return render(request , "formulario.html")
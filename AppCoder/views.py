from django.shortcuts import render
#Importando el modelo dar de alta uno nuevo importando la clase curso
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario


# Create my views here.
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

#VER CURSOS
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

#ALUMNOS
def alumnos(request):
    return render(request, "alumnos.html")


#PROFESORES
def profesores(request):
    return render(request, "profesores.html")


#DAR DE ALTA UN CURSO
def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")

#BUSCAR UN CURSO
def buscar_curso (request):
    return render(request, "buscar_curso.html")

#BUSCAR
def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
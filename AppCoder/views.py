from django.shortcuts import render
#Importando el modelo dar de alta uno nuevo importando la clase curso
from AppCoder.models import Curso
from AppCoder.models import Alumnos
from AppCoder.models import Profesores
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, Alumnos_formulario, Profesores_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


# Create my views here.
#4 Definir las views

#Responder en la platilla renderizada
def inicio(request):
    return render(request, "padre.html")


def alta_curso(request, nombre):
    #contructor de la clase, un objeto mas lo que hereda
    curso = Curso(nombre=nombre, ID_curso= 234512)
    curso.save()
    
    #Dar de alta los registros en la base de datos para insertarlos desde la interfaz
    texto=f"Se guardo en la DB el curso: {curso.nombre} {curso.ID_curso}"
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


#DAR DE ALTA UN CURSO  OCUPO ESTOOOOOOOOOOO
def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , ID_curso=datos["ID_curso"])
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
    
    
#FORMULARIO DE ALUMNOS
def nuevos_alumnos(request):

    if request.method == "POST":

        formulario_al = Alumnos_formulario( request.POST )
        if formulario_al.is_valid():
            datos = formulario_al.cleaned_data
            curso = Alumnos( nombre_alumno= datos["nombre_alumno"], curso_inscrito = datos["curso_inscrito"])
            curso.save()
            return render(request , "nuevos_alumnos.html")
        
    return render(request , "nuevos_alumnos.html")



#FORMULARIO DE PROFESORES
def nuevos_profesores(request):

    if request.method == "POST":

        formulario_prof = Profesores_formulario( request.POST )
        if formulario_prof.is_valid():
            datos = formulario_prof.cleaned_data
            curso = Profesores( nombre_profesor= datos["nombre_profesor"], curso_impartido = datos["curso_impartido"])
            curso.save()
            return render(request , "nuevos_profesores.html")
        
    return render(request , "nuevos_profesores.html")

#ELIMNAR CURSO
def eliminar_curso(request,id):
    curso=Curso.objects.get(id=id)
    curso.delete()
    curso=Curso.objects.all()
    return render(request, "cursos.html", {"cursos":curso})

#en la url llega el numero enfocada en la view, con get de la base de datos, elimina con delete en base de datos y obtieme la base de datos de nuevo renderizando con la base de datos

#EDITAR UN CURSO
#view tiene 2 comportamientos, cuando sea post y se redirecciona y cuando sea get y es cuando se clike editar, y genera un formulario, teniendo los valores iniciales llenando los datos con mi_formulario y haciendo un render con el template y mandar un diccionario con formulario y id

def editar(request,id):
    curso=Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario=Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso.nombre=datos["nombre"]
            curso.ID_curso=datos["ID_curso"]
            curso.save()
            
            curso=Curso.objects.all()
            return render(request, "cursos.html", {"cursos":curso})

    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre, "ID":curso.ID_curso})
        
    return render(request, "editar_curso.html", {"mi_formulario":mi_formulario, "curso":curso})


#LOGIN REQUEST
#Generar una nueva url y con login, y la peticion ser a get y el if no se ejecutara habiendo validacion, y como se hatra get 
#se hara un formulario para el usuario y hara un render para mostar el formulario y mandar template, y cargarlo desde padre

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            passw= form.cleaned_data.get("password") 
            user= authenticate(username = usuario, password = passw)
            
            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido/a {usuario}"})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO{form}")
            
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})


#REGISTRO
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario Registrado")
    
    
    else:
        form=UserCreationForm()
    return render(request, "registro.html", {"form":form})

#EDITAR PERFIL
def editar_perfil(request):
    usuario= request.user
    
    if request.method =="POST":
        mi_formulario= UserEditForm(request.POST)
        if mi_formulario.is_valid():
            informacion= mi_formulario.cleaned_data             #Cleaned_data : Return un diccionario propiedad:valor
            usuario.email = informacion["email"]
            password=informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request, "inicio.html")
    
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "editar_perfil.html", {"miFormulario":miFormulario, "usuario": usuario})
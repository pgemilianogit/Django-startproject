from django.shortcuts import render , redirect
#Importando el modelo dar de alta uno nuevo importando la clase curso
from AppCoder.models import Curso, Avatar, Alumnos, Profesores
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, Alumnos_formulario, Profesores_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required   #views que se pueda ver al iniciar sesion

# Create my views here.
#4 Definir las views

#Responder en la platilla renderizada
def inicio(request):
    return render(request, "padre.html")

# <---------------------------------- CRUD CURSOS ---------------------------------->

def alta_curso(request, nombre):
    #contructor de la clase, un objeto mas lo que hereda
    curso = Curso(nombre=nombre, ID_curso= 234512)
    curso.save()
    
    #Dar de alta los registros en la base de datos para insertarlos desde la interfaz
    texto=f"Se guardo en la DB el curso: {curso.nombre} {curso.ID_curso}"
    return HttpResponse(texto)

#VER CURSOS
@login_required
def ver_cursos(request): 
    #Como ver la base de datos, return lista
    cursos = Curso.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "cursos.html", {"url":avatares[0].imagen.url, "cursos":cursos})

"""dicc ={"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    #Loader simpl todo el problema de como entrar al template, donde ya definimos
    documento=plantilla.render(dicc)
    return HttpResponse(documento)"""
    
#DAR DE ALTA UN CURSO  OCUPO ESTOOOOOOOOOOO
def curso_formulario(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , ID_curso=datos["ID_curso"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html", {"url":avatares[0].imagen.url,})

#BUSCAR UN CURSO
def buscar_curso (request):
    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, "buscar_curso.html", {"url":avatares[0].imagen.url,})

#BUSCAR
def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
    
    
# <---------------------------------- CRUD PROFESORES ---------------------------------->

#PROFESORES
@login_required
def profesores(request):

    profes = Profesores.objects.all()
    avatares = Avatar.objects.filter(user=request.user)
    avatar_url = avatares[0].imagen.url if avatares.exists() else None
    cursos = Curso.objects.all()    
    context = {
        "profesores": profes,
        "url": avatar_url,
        "cursos": cursos
    }

    return render(request, "profesores.html", context)

    #EDITAR PROFESOR

@login_required
def editar_profesor(request, id):


    profesor = Profesores.objects.get(id=id)  # Obtiene el profesor por su ID
    if request.method == "POST":
        formulario = Profesores_formulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            profesor.nombre_profesor = datos['nombre_profesor']
            profesor.curso_impartido = datos['curso_impartido']
            profesor.save()
            return redirect('profesores')  # Redirige a la vista de profesores
    else:
        # Inicializa el formulario con los datos del profesor existente
        datos_iniciales = {
            'nombre_profesor': profesor.nombre_profesor,
            'curso_impartido': profesor.curso_impartido
        }
        formulario = Profesores_formulario(initial=datos_iniciales)

    return render(request, "editar_profesor.html", {"formulario": formulario, "profesor": profesor})

#BUSCAR PROFESOR
@login_required
def buscar_profesores(request):
    if 'nombre_profesor' in request.GET:
        nombre_profesor = request.GET["nombre_profesor"]
        profesores = Profesores.objects.filter(nombre_profesor__icontains=nombre_profesor)
        return render(request, "resultado_busqueda_profesores.html", {"profesores": profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor")

#ELIMINAR PROFESORES
@login_required
def baja_profesor(request, id):
    profe=Profesores.objects.get(id=id)
    profe.delete()
    profe=Profesores.objects.all()
    return render(request, "profesores.html", {"profesores":profe})


#ELIMINAR ALUMNOS
def baja_alumnos(request, id):
    alum=Alumnos.objects.get(id=id)
    alum.delete()
    alum=Alumnos.objects.all()
    return render(request, "alumnos.html", {"alums":alum})

#PROCESO:

#crear un diccionario con una sola propiedad (cursos) y el valor sera el conjunto de dicc
#teniendo todos los cursos cargar la plantilla  get_template metodo del motor de plantillas apuntando en settings
#render de la plantilla mandando el diccionario, pasa todo dinamismo, retorna todos los cursos

# <---------------------------------- CRUD ALUMNOS ---------------------------------->


#ALUMNOS
"""def alumnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "alumnos.html", {"url":avatares[0].imagen.url,})"""

#BUSCAR ALUMNOS
def buscar_alumnos(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profe = Alumnos.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"profe":profe})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
@login_required
def alumnos(request):
    """
    profesor= Profesores.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "profesores.html", {"url":avatares[0].imagen.url,})"""
    alum= Alumnos.objects.all()
    dicc={"alumnos": alum}
    plantilla=loader.get_template("alumnos.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)


    
    
#FORMULARIO DE ALUMNOS
def nuevos_alumnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":

        formulario_al = Alumnos_formulario( request.POST )
        if formulario_al.is_valid():
            datos = formulario_al.cleaned_data
            curso = Alumnos( nombre_alumno= datos["nombre_alumno"], curso_inscrito = datos["curso_inscrito"])
            curso.save()
            return render(request , "nuevos_alumnos.html")
        
    return render(request , "nuevos_alumnos.html", {"url":avatares[0].imagen.url,})



#FORMULARIO DE PROFESORES
@login_required
def nuevos_profesores(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        formulario_prof = Profesores_formulario(request.POST)
        if formulario_prof.is_valid():
            datos = formulario_prof.cleaned_data
            Profesores.objects.create(nombre_profesor=datos["nombre_profesor"], curso_impartido=datos["curso_impartido"])
            return redirect('profesores')  # Redirige para evitar doble post
    return render(request, "nuevos_profesores.html", {"url":avatares[0].imagen.url})


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
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html", {"url":avatares[0].imagen.url,})
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
    avatares = Avatar.objects.filter(user=request.user.id)

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

    return render(request, "editar_perfil.html", {"miFormulario" : miFormulario, "usuario" : usuario})
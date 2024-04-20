from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns= [      #name va relacionado con el padre para las direcciones
    path("", views.inicio, name="home"),
    path("buscar", views.buscar),
    path("buscar_alumnos", views.buscar_alumnos, name="BuscarAlumnos"),
    path("buscar_profesores", views.buscar_profesores, name="BuscarProfesores"),

 
 #PROFESORES
    path("profesores", views.profesores, name="profesores"),
    path("agregar_profesores", views.nuevos_profesores, name="AgregarProfesor"),
    path("baja_profesores/<int:id>", views.baja_profesor, name="baja_profesores"),
    path("editar_profesor/<int:id>", views.editar_profesor, name= "EditarProfesor"),
    
#ALUMNOS
    path("alumnos", views.alumnos , name="alumnos"),
    path("agregar_alumno", views.nuevos_alumnos, name="AgregarAlumno"),
    path("baja_alumnos/<int:id>", views.baja_alumnos, name="BajaAlumnos"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="EditarAlumno"),

#CURSOS
    path("alta_curso", views.curso_formulario),
    path("buscar_curso",views.buscar_curso, name="BuscarCurso"),
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"),
    path("editar_curso/<int:id>", views.editar, name="editar_curso"),
    path("ver_cursos", views.ver_cursos, name="Cursos"),

#LOGIN
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editar_perfil", views.editar_perfil, name="EditarPerfil"),
    
    #NOTAS
    #EDITAR ALUMNO
    #BORRAR ALUMNNO
]
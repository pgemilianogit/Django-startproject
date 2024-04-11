from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns= [      #name va relacionado con el padre para las direcciones
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="Cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("profesores", views.profesores, name="profesores"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso",views.buscar_curso),
    path("buscar", views.buscar),
 
 #ALUMNOS Y PROFESORES
    path("agregar_estudiante", views.nuevos_alumnos),
    path("agregar_profesores", views.nuevos_profesores),
    
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"),
    path("editar_curso/<int:id>", views.editar, name="editar_curso"),
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    #View de Django
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("edtar_perfil", views.editar_perfil, name="EditarPerfil")
    
]
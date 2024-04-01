from django.urls import path
from . import views

urlpatterns= [      #name va relacionado con el padre para las direcciones
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="Cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("profesores", views.profesores, name="profesores"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso",views.buscar_curso),
    path("buscar", views.buscar)
    
]
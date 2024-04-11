from django.contrib import admin
from .models import *

admin.site.register(Avatar)
# Register your models here.

#Nombres con columna correspondiendte con hipervinculo
@admin.register(Curso)
class AppCoder(admin.ModelAdmin):
    list_display=('id', 'nombre', 'ID_curso')
    #ordering=('-nombre',) #ordering =('ID_curso','nombre')
    search_fields=('nombre','ID_curso')
    #list_editable=('nombre','ID_curso')
    list_display_links=('nombre',)
    list_filter=('nombre',)
    list_per_page=10
    #exclude=('ID_curso')

@admin.register(Alumnos)
class AppCoder(admin.ModelAdmin):
    list_display=('id', 'nombre_alumno', 'curso_inscrito')
    #ordering=('-nombre',) #ordering =('ID_curso','nombre')
    search_fields=('nombre_alumno','curso_inscrito')
    #list_editable=('nombre','ID_curso')
    list_display_links=('nombre_alumno',)
    list_filter=('nombre_alumno',)
    list_per_page=10
    #exclude=('ID_curso')

@admin.register(Profesores)
class AppCoder(admin.ModelAdmin):
    list_display=('id', 'nombre_profesor', 'curso_impartido')
    #ordering=('-nombre',) #ordering =('ID_curso','nombre')
    search_fields=('nombre_profesor','curso_impartido')
    #list_editable=('nombre','ID_curso')
    list_display_links=('nombre_profesor',)
    list_filter=('nombre_profesor',)
    list_per_page=10
    #exclude=('ID_curso')


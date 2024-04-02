#Crear un formulario de tipo curso
#Al usar los formularios de django sera una clase que se heredara paara formulario con muchos metodos
from django import forms

class Curso_formulario(forms.Form):
        
        nombre = forms.CharField(max_length=30)
        ID_curso = forms.IntegerField()
    
class Alumnos_formulario(forms.Form):
    
    nombre_alumno = forms.CharField(max_length=30)
    curso_inscrito = forms.IntegerField()
    
class Profesores_formulario(forms.Form):
    
    nombre_profesor = forms.CharField(max_length=30)
    curso_impartido = forms.IntegerField()
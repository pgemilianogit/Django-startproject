#Crear un formulario de tipo curso
#Al usar los formularios de django sera una clase que se heredara paara formulario con muchos metodos
from django import forms

class Curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
#Crear un formulario de tipo curso
#Al usar los formularios de django sera una clase que se heredara paara formulario con muchos metodos
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm       #Formulario para crear usuarios

class Curso_formulario(forms.Form):
        
        nombre = forms.CharField(max_length=30)
        ID_curso = forms.IntegerField()
    
class Alumnos_formulario(forms.Form):
    
    nombre_alumno = forms.CharField(max_length=30)
    curso_inscrito = forms.IntegerField()
    
class Profesores_formulario(forms.Form):
    
    nombre_profesor = forms.CharField(max_length=30)
    curso_impartido = forms.IntegerField()
    
class UserEditForm(UserCreationForm):
    email= forms.EmailField(label="Modificar")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ['email', 'password1', 'password2']
        help_text={k:"" for k in fields }
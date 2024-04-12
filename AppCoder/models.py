from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Crear clase modulo Heredando de la clase padre para funcionalidad
class Curso(models.Model):
    
    #1. Estructura de datos donde el modelo es una clase y como se almacenaran los datos en la DB (SQL)
    #2. Clase18 Settings.py y en ISTALLED_APP
    nombre= models.CharField(max_length=40)
    ID_curso=models.IntegerField()
    
    #Mejor vista en admin para ver el curso y numero de ID_curso
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre, self.ID_curso)
    
    
    
class Alumnos(models.Model):
    nombre_alumno=models.CharField(max_length=40)
    curso_inscrito=models.IntegerField()

# Si el curso_impartido es una relación con otro modelo, usar un ForeignKey en lugar de un IntegerField.
class Profesores(models.Model):
    nombre_profesor=models.CharField(max_length=40)
    curso_impartido=models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    
class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="avatares", null=True, blank=True)
    
    def __str__(self):
        return f"User: {self.user} - Imagen: {self.imagen}"
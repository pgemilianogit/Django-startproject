from django.db import models

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
    
class Profesores(models.Model):
    nombre_profesor=models.CharField(max_length=40)
    curso_impartido=models.IntegerField()
    
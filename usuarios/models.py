from django.db import models

# Create your models here.
class Usuario(models.Model):
    NombreUsuario = models.CharField(max_length=100, unique=True)
    Contrasena = models.CharField(max_length=100)
    Rol = models.CharField(max_length=50)

    def __str__(self):
        return self.NombreUsuario

class Auditoria(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Fecha = models.DateTimeField()
    Accion = models.CharField(max_length=200)

    def __str__(self):
        return f"Acción: {self.Accion}"
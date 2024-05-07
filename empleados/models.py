from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Departamento(models.Model):
    NombreDepartamento = models.CharField(max_length=100)

    def __str__(self):
        return self.NombreDepartamento

class Cargo(models.Model):
    NombreCargo = models.CharField(max_length=100)

    def __str__(self):
        return self.NombreCargo

class Empleado(models.Model):
    EmpleadoID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Cedula = models.IntegerField(null=True, blank=True)
    ARL = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"

class Nomina(models.Model):
    NominaID = models.IntegerField(primary_key=True)
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    Sueldo = models.FloatField()
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    FechaIngreso = models.DateField()
    EPS = models.CharField(max_length=100)
    FondoPension = models.CharField(max_length=100)

    def __str__(self):
        return f"Nómina {self.NominaID}"

class Novedad(models.Model):
    Descripcion = models.CharField(max_length=100)
    Fecha = models.DateField()
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return self.Descripcion
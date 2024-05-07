from django.db import models

# Create your models here.
class Pelicula(models.Model):
    Titulo = models.CharField(max_length=200)
    AnioLanzamiento = models.IntegerField()
    Duracion = models.TimeField()
    Calificacion = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.Titulo

class GeneroPelicula(models.Model):
    NombreGenero = models.CharField(max_length=100)
    Peliculas = models.ManyToManyField(Pelicula, through='PeliculaGenero')

    def __str__(self):
        return self.NombreGenero

class PeliculaGenero(models.Model):
    Pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    GeneroPelicula = models.ForeignKey(GeneroPelicula, on_delete=models.CASCADE)

class Libro(models.Model):
    Titulo = models.CharField(max_length=200)
    AnioPublicacion = models.IntegerField()
    Calificacion = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.Titulo

class GeneroLibro(models.Model):
    NombreGenero = models.CharField(max_length=100)
    Libros = models.ManyToManyField(Libro, through='LibroGenero')

    def __str__(self):
        return self.NombreGenero

class LibroGenero(models.Model):
    Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    GeneroLibro = models.ForeignKey(GeneroLibro, on_delete=models.CASCADE)

class Autor(models.Model):
    NombreAutor = models.CharField(max_length=100)
    Libros = models.ManyToManyField(Libro, through='LibroAutor')

    def __str__(self):
        return self.NombreAutor

class LibroAutor(models.Model):
    Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
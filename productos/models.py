from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    anio_lanzamiento = models.IntegerField()

    def __str__(self):
        return self.titulo

class GeneroPelicula(models.Model):
    nombre_genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_genero

class PeliculaGenero(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    genero = models.ForeignKey(GeneroPelicula, on_delete=models.CASCADE)





#Libros

class Autor(models.Model):
    nombre_autor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_autor

class GeneroLibro(models.Model):
    nombre_genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_genero

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    isbn13 = models.CharField(max_length=17, blank=True, null=True)
    codigo_idioma = models.CharField(max_length=5, blank=True, null=True)
    numero_paginas = models.IntegerField(blank=True, null=True)
    cantidad_calificaciones = models.IntegerField(blank=True, null=True)
    cantidad_resenas = models.IntegerField(blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)
    editorial = models.CharField(max_length=100, blank=True, null=True)
    anio_publicacion = models.IntegerField()
    calificacion = models.DecimalField(max_digits=3, decimal_places=2)


    autores = models.ManyToManyField(Autor, through='LibroAutor')
    generos = models.ManyToManyField(GeneroLibro, through='LibroGenero')

    def __str__(self):
        return self.titulo

class LibroAutor(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('libro', 'autor')

class LibroGenero(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    genero = models.ForeignKey(GeneroLibro, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('libro', 'genero')
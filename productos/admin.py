from django.contrib import admin
from .models import Pelicula, GeneroPelicula, PeliculaGenero, Autor, GeneroLibro, Libro, LibroAutor, LibroGenero

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(GeneroPelicula)
admin.site.register(PeliculaGenero)

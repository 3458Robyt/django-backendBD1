from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PeliculaSerializer, GeneroLibroSerializer, GeneroPeliculaSerializer, LibroSerializer, LibroAutorSerializer, LibroGeneroSerializer, AutorSerializer, PeliculaGeneroSerializer
from .models import Pelicula, GeneroLibro, GeneroPelicula, Libro, LibroAutor, LibroGenero, Autor, PeliculaGenero

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class GeneroPeliculaViewSet(viewsets.ModelViewSet):
    queryset = GeneroPelicula.objects.all()
    serializer_class = GeneroPeliculaSerializer

class PeliculaGeneroViewSet(viewsets.ModelViewSet):
    queryset = PeliculaGenero.objects.all()
    serializer_class = PeliculaGeneroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class GeneroLibroViewSet(viewsets.ModelViewSet):
    queryset = GeneroLibro.objects.all()
    serializer_class = GeneroLibroSerializer

class LibroGeneroViewSet(viewsets.ModelViewSet):
    queryset = LibroGenero.objects.all()
    serializer_class = LibroGeneroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroAutorViewSet(viewsets.ModelViewSet):
    queryset = LibroAutor.objects.all()
    serializer_class = LibroAutorSerializer


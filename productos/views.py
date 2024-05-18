from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PeliculaSerializer, GeneroPeliculaSerializer, PeliculaGeneroSerializer, AutorSerializer, LibroSerializer, AutorLibroSerializer
from .models import Pelicula, GeneroPelicula, PeliculaGenero, Autor, Libro, AutorLibro

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class GeneroPeliculaViewSet(viewsets.ModelViewSet):
    queryset = GeneroPelicula.objects.all()
    serializer_class = GeneroPeliculaSerializer

class PeliculaGeneroViewSet(viewsets.ModelViewSet):
    queryset = PeliculaGenero.objects.all()
    serializer_class = PeliculaGeneroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class AutorLibroViewSet(viewsets.ModelViewSet):
    queryset = AutorLibro.objects.all()
    serializer_class = AutorLibroSerializer


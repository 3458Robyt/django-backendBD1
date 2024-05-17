from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PeliculaSerializer, GeneroLibroSerializer, GeneroPeliculaSerializer, LibroSerializer, LibroAutorSerializer, LibroGeneroSerializer, AutorSerializer, PeliculaGeneroSerializer
from .models import Pelicula, GeneroLibro, GeneroPelicula, Libro, LibroAutor, LibroGenero, Autor, PeliculaGenero
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db import connection

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


class InformacionPeliculaViewSet(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute("CALL informacion_peliculas()")
            resultados = cursor.fetchall()

        # Procesar los resultados según sea necesario
        # Por ejemplo, formatearlos utilizando un serializador
        data = self.procesar_resultados(resultados)

        return Response(data)

    def procesar_resultados(self, resultados):
        # Procesa los resultados según sea necesario
        # Por ejemplo, formatearlos utilizando un serializador
        processed_data = []
        for resultado in resultados:
            processed_data.append({
                'pelicula_id': resultado[0],
                'titulo': resultado[1],
                'anio_lanzamiento': resultado[2],
                'nombre_genero': resultado[3]
            })
        return processed_data